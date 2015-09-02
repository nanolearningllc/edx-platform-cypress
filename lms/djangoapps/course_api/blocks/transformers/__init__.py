"""
Course API Block Transformers
"""

from student_view import StudentViewTransformer

SUPPORTED_FIELDS = (
    (None, 'type'),
    (None, 'display_name'),
    (None, 'graded'),
    (None, 'format'),

    (StudentViewTransformer, StudentViewTransformer.STUDENT_VIEW_DATA),
    (StudentViewTransformer, StudentViewTransformer.STUDENT_VIEW_MULTI_DEVICE),
)
