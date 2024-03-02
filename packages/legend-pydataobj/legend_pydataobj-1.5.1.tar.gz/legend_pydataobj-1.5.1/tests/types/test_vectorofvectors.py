from __future__ import annotations

import awkward as ak
import awkward_pandas as akpd
import numpy as np
import pandas as pd
import pint
import pytest

import lgdo
from lgdo import VectorOfVectors, utils
from lgdo.types import vectorofvectors as vov


@pytest.fixture()
def lgdo_vov():
    return VectorOfVectors(
        flattened_data=lgdo.Array(
            nda=np.array([1, 2, 3, 4, 5, 2, 4, 8, 9, 7, 5, 3, 1])
        ),
        cumulative_length=lgdo.Array(nda=np.array([2, 5, 6, 10, 13])),
    )
    # [1 2]
    # [3 4 5]
    # [2]
    # [4 8 9 7]
    # [5 3 1]


def test_init(lgdo_vov):
    assert len(VectorOfVectors(dtype="ubyte")) == 0

    v = VectorOfVectors(shape_guess=(10, 20), dtype="int32", fill_val=2)
    assert v.flattened_data == lgdo.Array(shape=(10 * 20,), fill_val=2, dtype="int32")
    assert v.cumulative_length == lgdo.Array(
        np.arange(20, 10 * 20 + 1, 20, dtype="uint32")
    )

    test = VectorOfVectors([[1, 2], [3, 4, 5], [2], [4, 8, 9, 7], [5, 3, 1]])
    assert test == lgdo_vov
    assert len(test) == 5

    v = VectorOfVectors(
        cumulative_length=np.array([5, 10, 15], dtype="uint32"), dtype="ubyte"
    )
    assert len(v.flattened_data) == 15
    assert len(v[-1]) == 5

    v = VectorOfVectors(shape_guess=(5, 0), dtype="int32")
    assert v.cumulative_length == lgdo.Array([0, 0, 0, 0, 0])

    v = VectorOfVectors(ak.Array([[1, 2], [3, 4, 5], [2], [4, 8, 9, 7], [5, 3, 1]]))
    assert v == test


def test_datatype_name(lgdo_vov):
    assert lgdo_vov.datatype_name() == "array"


def test_form_datatype(lgdo_vov):
    assert lgdo_vov.form_datatype() == "array<1>{array<1>{real}}"


def test_values(lgdo_vov):
    desired = [
        np.array([1, 2]),
        np.array([3, 4, 5]),
        np.array([2]),
        np.array([4, 8, 9, 7]),
        np.array([5, 3, 1]),
    ]

    for i in range(len(desired)):
        assert np.array_equal(desired[i], lgdo_vov[i])

    assert np.array_equal(lgdo_vov[-1], desired[-1])
    assert np.array_equal(lgdo_vov[-2], desired[-2])

    v = VectorOfVectors([[1, 2]], dtype="uint32")
    assert np.array_equal(v[-1], [1, 2])


def test_resize(lgdo_vov):
    lgdo_vov.resize(3)
    assert len(lgdo_vov.cumulative_length) == 3
    assert len(lgdo_vov.flattened_data) == lgdo_vov.cumulative_length[-1]

    desired = [np.array([1, 2]), np.array([3, 4, 5]), np.array([2])]

    for i in range(len(lgdo_vov)):
        assert np.array_equal(desired[i], lgdo_vov[i])

    lgdo_vov.resize(5)
    assert len(lgdo_vov) == 5
    assert len(lgdo_vov[3]) == 0
    assert len(lgdo_vov[4]) == 0
    assert lgdo_vov == VectorOfVectors([[1, 2], [3, 4, 5], [2], [], []])

    v = VectorOfVectors(dtype="i")
    v.resize(3)
    assert v == VectorOfVectors([[], [], []], dtype="i")


def test_aoesa(lgdo_vov):
    arr = lgdo_vov.to_aoesa()
    desired = np.array(
        [
            [1, 2, np.nan, np.nan],
            [3, 4, 5, np.nan],
            [2, np.nan, np.nan, np.nan],
            [4, 8, 9, 7],
            [5, 3, 1, np.nan],
        ]
    )
    assert isinstance(arr, lgdo.ArrayOfEqualSizedArrays)
    assert np.issubdtype(arr.dtype, np.floating)
    assert np.array_equal(arr.nda, desired, True)

    v = VectorOfVectors(
        flattened_data=lgdo.Array(
            nda=np.array([1, 2, 3, 4, 5, 2, 4, 8, 9, 7, 5, 3, 1], dtype="int16")
        ),
        cumulative_length=lgdo.Array(nda=np.array([2, 5, 6, 10, 13])),
    )
    aoesa = v.to_aoesa()

    assert np.issubdtype(aoesa.dtype, np.floating)

    aoesa = v.to_aoesa(fill_val=-999.9)
    assert np.issubdtype(aoesa.nda.dtype, np.floating)

    aoesa = v.to_aoesa(fill_val=-999)
    assert np.issubdtype(aoesa.nda.dtype, np.integer)

    aoesa = v.to_aoesa(fill_val=-999, preserve_dtype=True)
    assert aoesa.nda.dtype == np.int16


def test_set_vector(lgdo_vov):
    lgdo_vov[0] = np.zeros(2)

    desired = [
        np.zeros(2),
        np.array([3, 4, 5]),
        np.array([2]),
        np.array([4, 8, 9, 7]),
        np.array([5, 3, 1]),
    ]

    for i in range(len(desired)):
        assert np.array_equal(desired[i], lgdo_vov[i])

    with pytest.raises(ValueError):
        lgdo_vov[0] = np.zeros(3)

    lgdo_vov[1] = np.zeros(3)

    desired = [
        np.zeros(2),
        np.zeros(3),
        np.array([2]),
        np.array([4, 8, 9, 7]),
        np.array([5, 3, 1]),
    ]

    for i in range(len(desired)):
        assert np.array_equal(desired[i], lgdo_vov[i])


def test_append(lgdo_vov):
    lgdo_vov.append(np.zeros(3))
    assert np.array_equal(lgdo_vov[-1], np.zeros(3))

    v = VectorOfVectors(dtype="int64")
    v.append(np.zeros(3))
    assert v == VectorOfVectors([[0, 0, 0]])


def test_insert(lgdo_vov):
    lgdo_vov.insert(2, np.zeros(3))
    assert lgdo_vov == VectorOfVectors(
        [
            [1, 2],
            [3, 4, 5],
            [0, 0, 0],
            [2],
            [4, 8, 9, 7],
            [5, 3, 1],
        ]
    )

    v = VectorOfVectors(shape_guess=(3, 5), dtype="int32", fill_val=0)
    v.insert(2, [1, 2, 3])
    assert np.array_equal(v.cumulative_length, [5, 10, 13, 18])
    assert np.array_equal(v[2], [1, 2, 3])


def test_replace(lgdo_vov):
    v = utils.copy(lgdo_vov)
    v.replace(1, np.zeros(3))
    assert v == VectorOfVectors(
        [
            [1, 2],
            [0, 0, 0],
            [2],
            [4, 8, 9, 7],
            [5, 3, 1],
        ]
    )

    v = utils.copy(lgdo_vov)
    v.replace(1, np.zeros(2))
    assert v == VectorOfVectors(
        [
            [1, 2],
            [0, 0],
            [2],
            [4, 8, 9, 7],
            [5, 3, 1],
        ]
    )

    v = utils.copy(lgdo_vov)
    v.replace(1, np.zeros(4))
    assert v == VectorOfVectors(
        [
            [1, 2],
            [0, 0, 0, 0],
            [2],
            [4, 8, 9, 7],
            [5, 3, 1],
        ]
    )


def test_set_vector_unsafe(lgdo_vov):
    desired = [
        np.array([1, 2], dtype=lgdo_vov.dtype),
        np.array([3, 4, 5], dtype=lgdo_vov.dtype),
        np.array([2], dtype=lgdo_vov.dtype),
        np.array([4, 8, 9, 7], dtype=lgdo_vov.dtype),
        np.array([5, 3, 1], dtype=lgdo_vov.dtype),
    ]
    desired_aoa = np.zeros(shape=(5, 5), dtype=lgdo_vov.dtype)
    desired_lens = np.array([len(arr) for arr in desired])

    # test sequential filling
    second_vov = lgdo.VectorOfVectors(shape_guess=(5, 5), dtype=lgdo_vov.dtype)
    for i, arr in enumerate(desired):
        second_vov._set_vector_unsafe(i, arr)
        desired_aoa[i, : len(arr)] = arr
    assert lgdo_vov == second_vov

    # test vectorized filling
    third_vov = lgdo.VectorOfVectors(shape_guess=(5, 5), dtype=lgdo_vov.dtype)
    third_vov._set_vector_unsafe(0, desired_aoa, desired_lens)
    assert lgdo_vov == third_vov


def test_iter(lgdo_vov):
    desired = [[1, 2], [3, 4, 5], [2], [4, 8, 9, 7], [5, 3, 1]]

    c = 0
    for v in lgdo_vov:
        assert np.array_equal(v, desired[c])
        c += 1


def test_build_cl_and_explodes():
    cl = np.array([3, 4], dtype=np.uint64)
    exp = np.array([0, 0, 0, 1], dtype=np.uint64)
    array = np.array([5, 7], dtype=np.uint64)
    array_exp = np.array([5, 5, 5, 7], dtype=np.uint64)
    # build_cl
    assert (vov.build_cl(exp, cl) == cl).all()
    assert (vov.build_cl(exp) == cl).all()
    assert (vov.build_cl([0, 0, 0, 1]) == cl).all()
    assert (vov.build_cl(array_exp, cl) == cl).all()
    assert (vov.build_cl(array_exp) == cl).all()
    assert (vov.build_cl([5, 5, 5, 7]) == cl).all()
    # explode_cl
    assert (vov.explode_cl(cl, exp) == exp).all()
    assert (vov.explode_cl(cl) == exp).all()
    assert (vov.explode_cl([3, 4]) == exp).all()
    # inverse functionality
    assert (vov.build_cl(vov.explode_cl(cl)) == cl).all()
    assert (vov.explode_cl(vov.build_cl(array_exp)) == exp).all()
    # explode
    assert (vov.explode(cl, array, array_exp) == array_exp).all()
    assert (vov.explode(cl, array) == array_exp).all()
    assert (vov.explode([3, 4], [5, 7]) == array_exp).all()
    assert (vov.explode(cl, range(len(cl))) == exp).all()
    # explode_arrays
    arrays_out = vov.explode_arrays(cl, [array, range(len(cl))])
    assert len(arrays_out) == 2
    assert (arrays_out[0] == array_exp).all()
    assert (arrays_out[1] == exp).all()
    arrays_out = vov.explode_arrays(cl, [array, range(len(cl))], arrays_out=arrays_out)
    assert len(arrays_out) == 2
    assert (arrays_out[0] == array_exp).all()
    assert (arrays_out[1] == exp).all()


def test_copy(lgdo_vov):
    assert lgdo_vov == utils.copy(lgdo_vov)


def test_view(lgdo_vov):
    lgdo_vov.attrs["units"] = "s"
    with pytest.raises(ValueError):
        lgdo_vov.view_as("ak", with_units=True)

    ak_arr = lgdo_vov.view_as("ak", with_units=False)

    assert isinstance(ak_arr, ak.Array)
    assert len(ak_arr) == len(lgdo_vov)
    assert ak.all(ak_arr == [[1, 2], [3, 4, 5], [2], [4, 8, 9, 7], [5, 3, 1]])

    np_arr = lgdo_vov.view_as("np", with_units=True)
    assert isinstance(np_arr, pint.Quantity)
    assert np_arr.u == "second"
    assert isinstance(np_arr.m, np.ndarray)

    np_arr = lgdo_vov.view_as("np", with_units=False)
    assert isinstance(np_arr, np.ndarray)
    assert np.issubdtype(np_arr.dtype, np.floating)

    np_arr = lgdo_vov.view_as("np", with_units=False, fill_val=0, preserve_dtype=True)
    assert np.issubdtype(np_arr.dtype, np.integer)

    np_arr = lgdo_vov.view_as("pd", with_units=False)
    assert isinstance(np_arr, pd.Series)
    assert isinstance(np_arr.ak, akpd.accessor.AwkwardAccessor)
