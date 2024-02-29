# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2024 Baidu.com, Inc. All Rights Reserved
"""
Vistudio Spec
"""
from typing import List, Tuple, Any
import pyarrow as pa
from pydantic import BaseModel


class Label(BaseModel):
    """Label"""
    id: int
    name: str
    confidence: float

    @classmethod
    def get_data_type(cls) -> pa.DataType:
        """Label to pyarrow data type"""
        return pa.struct([
            ("id", pa.int32()), 
            ("name", pa.string()), 
            ("confidence", pa.float32())
        ])


class OCR(BaseModel):
    """OCR"""
    word: str
    direction: str

    @classmethod
    def get_data_type(cls) -> pa.DataType:
        """OCR to pyarrow data type"""
        return pa.struct([
            ("word", pa.string()), 
            ("direction", pa.string())
        ])


class RLE(BaseModel):
    """RLE"""
    counts: List[float]
    size: Tuple[float, float]

    @classmethod
    def get_data_type(cls) -> pa.DataType:
        """RLE to pyarrow data type"""
        return pa.struct([
            ("count", pa.list_(pa.float32())), 
            ("size", pa.list_(pa.float32()))
        ])


class Annotation(BaseModel):
    """Annotation"""
    id: int
    bbox: List[float]
    segmentation: List[float]
    rle: RLE
    keypoints: List[float]
    ocr: OCR
    area: float
    labels: List[Label]

    @classmethod
    def get_data_type(cls) -> pa.DataType:
        """Annotation to pyarrow data type"""
        return pa.struct([
            ("id", pa.int32()),
            ("bbox", pa.list_(pa.float32())),
            ("segmentation", pa.list_(pa.float32())),
            ("rle", RLE.get_data_type()),
            ("keypoints", pa.list_(pa.float32())),
            ("ocr", OCR.get_data_type()),
            ("area", pa.float32()),
            ("labels", pa.list_(Label.get_data_type()))
        ])


class Annotations(BaseModel):
    """Annotations"""
    imageID: int
    modelName: str
    modelVersion: str
    annotations: List[Annotation]

    @classmethod
    def get_data_type(cls) -> pa.DataType:
        """Annotations to pyarrow data type"""
        return pa.struct([
            ("modelName", pa.string()), 
            ("modelVersion", pa.string()),
            ("annotations", pa.list_(Annotation.get_data_type()))
        ])


class Image(BaseModel):
    """Image"""
    id: int
    name: str
    fileUri: str
    width: int
    height: int

    @classmethod
    def get_data_type(cls) -> pa.DataType:
        """Image to pyarrow data type"""
        return pa.struct([
            ("id", pa.int32()),
            ("width", pa.int32()),
            ("height", pa.int32()),
            ("fileName", pa.string()),
        ])


class Vistudio(BaseModel):
    """Vistudio"""
    images: List[Image]
    annotations: List[Annotations]
    labels: List[Label]

    @classmethod
    def to_pyarrow_schema(cls) -> pa.Schema:
        """Vistudio to pyarrow schema"""
        return pa.schema([
            pa.field("images", Image.get_data_type()),
            pa.field("annotations", Annotations.get_data_type()),
            pa.field("labels", Label.get_data_type()),
        ])


if __name__ == "__main__":
    print(Vistudio.to_pyarrow_schema())

