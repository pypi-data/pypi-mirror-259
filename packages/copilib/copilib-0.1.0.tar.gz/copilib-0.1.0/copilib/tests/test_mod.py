"""
Copyright 2024 Weavers @ Eternal Loom. All rights reserved.
Use of this software is governed by the license that can be
found in LICENSE file in the source repository.
"""

# Copyright 2023 Weavers @ Eternal Loom. All rights reserved.
#
# Use of this software is governed by the license that can be
# found in LICENSE file in the source repository.


def test_module_import():
    """Test module import"""
    import copilib

    assert copilib is not None


def test_other_module_imports():
    """Test other module import"""
    import smartypes

    assert smartypes is not None
