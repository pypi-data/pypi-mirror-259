"""
Original code modified for Opteryx.
"""

import numpy
import pyarrow
from pyarrow import compute

from opteryx.compiled import list_ops

# Added for Opteryx, comparisons in filter_operators updated to match
# this set is from sqloxide
FILTER_OPERATORS = {
    "Eq",
    "NotEq",
    "Gt",
    "GtEq",
    "Lt",
    "LtEq",
    "Like",
    "ILike",
    "NotLike",
    "NotILike",
    "InList",
    "SimilarTo",
    "NotSimilarTo",
    "PGRegexMatch",
    "NotPGRegexMatch",
    "PGRegexNotMatch",
    "PGRegexIMatch",  # "~*"
    "NotPGRegexIMatch",  # "!~*"
    "PGRegexNotIMatch",  # "!~*"
    "BitwiseOr",  # |
}


def filter_operations(arr, operator, value):
    """
    Wrapped for Opteryx added to correctly handle null semantics.

    This returns an array with tri-state boolean (tue/false/none);
    if being used for display use as is, if being used for filtering, none is false.
    """

    # if the input is a table, get the first column
    if isinstance(value, pyarrow.Table):  # pragma: no cover
        value = value.column(0).to_numpy()

    morsel_size = len(arr)

    # compute null positions
    null_positions = numpy.logical_or(
        compute.is_null(arr, nan_is_null=True),
        compute.is_null(value, nan_is_null=True),
    )

    # Early exit if all values are null
    if null_positions.all():
        return pyarrow.array([None] * morsel_size, type=pyarrow.bool_())

    # Prepare for null-excluded evaluation
    valid_positions = ~null_positions

    compressed = False
    if (
        valid_positions.any()
        and isinstance(arr, numpy.ndarray)
        and isinstance(value, numpy.ndarray)
    ):
        # if we have nulls and both columns are numpy arrays, we can speed things
        # up by removing the nulls from the calculations, we add the rows back in
        # later
        arr = arr.compress(valid_positions)
        value = value.compress(valid_positions)
        compressed = True

    # do the evaluation
    results_mask = _inner_filter_operations(arr, operator, value)

    if compressed:
        # fill the result set
        results = numpy.array([None] * morsel_size, dtype=object)
        numpy.place(results, valid_positions, results_mask)

        # build tri-state response, PyArrow supports tristate, numpy does not
        return pyarrow.array(results, type=pyarrow.bool_())

    return results_mask


# Filter functionality
def _inner_filter_operations(arr, operator, value):
    """
    Execute filter operations, this returns an array of the indexes of the rows that
    match the filter
    """
    # ADDED FOR OPTERYX

    if operator == "Eq":
        return compute.equal(arr, value).to_numpy(False).astype(dtype=bool)
    if operator == "NotEq":
        return compute.not_equal(arr, value).to_numpy(False).astype(dtype=bool)
    if operator == "Lt":
        return compute.less(arr, value).to_numpy(False).astype(dtype=bool)
    if operator == "Gt":
        return compute.greater(arr, value).to_numpy(False).astype(dtype=bool)
    if operator == "LtEq":
        return compute.less_equal(arr, value).to_numpy(False).astype(dtype=bool)
    if operator == "GtEq":
        return compute.greater_equal(arr, value).to_numpy(False).astype(dtype=bool)
    if operator == "InList":
        # MODIFIED FOR OPTERYX
        # some of the lists are saved as sets, which are faster than searching numpy
        # arrays, even with numpy's native functionality - choosing the right algo
        # is almost always faster than choosing a fast language.
        return numpy.array([a in value[0] for a in arr], dtype=numpy.bool_)  # [#325]?
    if operator == "NotInList":
        # MODIFIED FOR OPTERYX - see comment above
        return numpy.array([a not in value[0] for a in arr], dtype=numpy.bool_)  # [#325]?
    if operator == "Like":
        # MODIFIED FOR OPTERYX
        # null input emits null output, which should be false/0
        return compute.match_like(arr, value[0]).to_numpy(False).astype(dtype=bool)  # [#325]
    if operator == "NotLike":
        # MODIFIED FOR OPTERYX - see comment above
        matches = compute.match_like(arr, value[0]).to_numpy(False).astype(dtype=bool)  # [#325]
        return numpy.invert(matches)
    if operator == "ILike":
        # MODIFIED FOR OPTERYX - see comment above
        return (
            compute.match_like(arr, value[0], ignore_case=True).to_numpy(False).astype(dtype=bool)
        )  # [#325]
    if operator == "NotILike":
        # MODIFIED FOR OPTERYX - see comment above
        matches = compute.match_like(arr, value[0], ignore_case=True)  # [#325]
        return numpy.invert(matches)
    if operator in ("PGRegexMatch", "SimilarTo", "RLike"):
        # MODIFIED FOR OPTERYX - see comment above
        return (
            compute.match_substring_regex(arr, value[0]).to_numpy(False).astype(dtype=bool)
        )  # [#325]
    if operator in ("PGRegexNotMatch", "NotSimilarTo", "NotRLike"):
        # MODIFIED FOR OPTERYX - see comment above
        matches = compute.match_substring_regex(arr, value[0])  # [#325]
        return numpy.invert(matches)
    if operator == "PGRegexIMatch":
        # MODIFIED FOR OPTERYX - see comment above
        return (
            compute.match_substring_regex(arr, value[0], ignore_case=True)
            .to_numpy(False)
            .astype(dtype=bool)
        )  # [#325]
    if operator == "PGRegexNotIMatch":
        # MODIFIED FOR OPTERYX - see comment above
        matches = compute.match_substring_regex(arr, value[0], ignore_case=True)  # [#325]
        return numpy.invert(matches)

    if operator == "AnyOpEq":
        return list_ops.cython_anyop_eq(arr[0], value)
    if operator == "AnyOpNotEq":
        return list_ops.cython_anyop_neq(arr[0], value)
    if operator == "AnyOpGt":
        return list_ops.cython_anyop_gt(arr[0], value)
    if operator == "AnyOpLt":
        return list_ops.cython_anyop_lt(arr[0], value)
    if operator == "AnyOpGtEq":
        return list_ops.cython_anyop_gte(arr[0], value)
    if operator == "AnyOpLtEq":
        return list_ops.cython_anyop_lte(arr[0], value)
    if operator == "AllOpEq":
        return list_ops.cython_allop_eq(arr[0], value)
    if operator == "AllOpNotEq":
        return list_ops.cython_allop_neq(arr[0], value)
    raise NotImplementedError(f"Operator {operator} is not implemented!")  # pragma: no cover
