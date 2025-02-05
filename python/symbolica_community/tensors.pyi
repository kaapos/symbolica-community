# This file is automatically generated by pyo3_stub_gen
# ruff: noqa: E501, F401

from __future__ import annotations

import typing
from enum import Enum
from typing import (
    Any,
    Callable,
    Iterator,
    List,
    Optional,
    Sequence,
    Tuple,
    overload,
)

from python.symbolica_community.symbolica_community import Expression

class CompiledTensorEvaluator:
    r"""
    A compiled and optimized evaluator for tensors.
    """

    def evaluate(self,inputs:Sequence[Sequence[float]])-> List[Tensor]:
        """Evaluate the expression for multiple inputs and return the result."""

    def evaluate_complex(self, inputs: Sequence[Sequence[complex]]) -> List[Tensor]:
        """Evaluate the expression for multiple complex inputs and return the result."""

class Representation:
    r"""
    A representation class in the sense of representation theory. This class is used to represent the representation of a tensor. It is essentially a pair of a name and a dimension.
    New representations are registered when constructing.
    Some representations are dualizable, meaning that they have a dual representation.
    Indices will only ever match across dual representations.
    There are some already registered representations, such as:
     EUCLIDEAN: Rep = Rep::SelfDual(0);
     BISPINOR: Rep = Rep::SelfDual(1);
     COLORADJ: Rep = Rep::SelfDual(2);
     MINKOWSKI: Rep = Rep::SelfDual(3);

     LORENTZ_UP: Rep = Rep::Dualizable(1);
     LORENTZ_DOWN: Rep = Rep::Dualizable(-1);
     SPINFUND: Rep = Rep::Dualizable(2);
     SPINANTIFUND: Rep = Rep::Dualizable(-2);
     COLORFUND: Rep = Rep::Dualizable(3);
     COLORANTIFUND: Rep = Rep::Dualizable(-3);
     COLORSEXT: Rep = Rep::Dualizable(4);
     COLORANTISEXT: Rep = Rep::Dualizable(-4);
    """
    def __new__(cls,name:str,dimension:int,dual:bool =False)->Representation:
        ...
    def __call__(self, aind:int|Expression|str) -> Slot:
        r"""
        Generate a new slot with the given index, from this representation
        """
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...

    def to_expression(self) -> Expression:
        r"""
        Return the symbolica expression of the representation.
        """

class Slot:
    r"""
    An abstract index slot for a tensor.
    This is essentially a tuple of a `Representation` and an abstract index id.

    The abstract index id can be either an integer or a symbol.
    This is the building block for creating tensor structures that can be contracted.
    """
    def __new__(cls,name:str,dimension:int,aind:int|str|Expression,dual:bool =False)->Slot:
        ...
    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...

    def to_expression(self) -> Expression:
        r"""
        Return the symbolica expression of the slot.
        """


class Tensor(Sequence):
    r"""
    A tensor class that can be either dense or sparse.
    The data is either float or complex or a symbolica expression
    It can be instantiated with data using the `sparse_empty` or `dense` module functions.
    """
    def structure(self) -> TensorStructure|TensorIndices:
        r"""
        Return the structure of the tensor.
        """

    def to_dense(self) -> None:
        r"""
        Convert the internal data storage to dense.
        """
    def __repr__(self) -> str:
            ...

    def __str__(self) -> str:
            ...

    def __len__(self) -> int:
        r"""
        Return the size of the tensor (product of dimensions).
        """

    @overload
    def __getitem__(self, idx: int) -> float|Expression: ...

    @overload
    def __getitem__(self, s: slice) -> Sequence[float|Expression]: ...

    @overload
    def __getitem__(self, key: List[int]) -> float|Expression:
        r"""
        Get the data stored at the given index (flattened) or indices (row-major).
        """

    def __setitem__(self, key: int|List[int], value: float|Expression) -> None:
        r"""
        Set the data stored at the given index (flattened) or indices (row-major).
        """

    def evaluator(
        self,
        constants: dict[Expression, Expression],
        funs: dict[Tuple[Expression, str, Sequence[Expression]], Expression],
        params: Sequence[Expression],
        iterations: int = 100,
        n_cores: int = 4,
        verbose: bool = False,
    ) -> TensorEvaluator:
        """Create an evaluator that can evaluate (nested) expressions in an optimized fashion.
        All constants and functions should be provided as dictionaries, where the function
        dictionary has a key `(name, printable name, arguments)` and the value is the function
        body. For example the function `f(x,y)=x^2+y` should be provided as
        `{(f, "f", (x, y)): x**2 + y}`. All free parameters should be provided in the `params` list.
        """

    def scalar(self)->Expression:
        r"""
        Unwrap the tensor into a scalar, if possible.
        """

class TensorEvaluator:
    r"""
    An optimized evaluator for tensors.
    """
    def evaluate(self,inputs:Sequence[Sequence[float]])-> List[Tensor]:
        """Evaluate the expression for multiple inputs and return the result."""

    def evaluate_complex(self, inputs: Sequence[Sequence[complex]]) -> List[Tensor]:
        """Evaluate the expression for multiple complex inputs and return the result."""

    def compile(
        self,
        function_name: str,
        filename: str,
        library_name: str,
        inline_asm: bool = True,
        optimization_level: int = 3,
        compiler_path: Optional[str] = None,
    ) -> CompiledTensorEvaluator:
        """Compile the evaluator to a shared library using C++ and optionally inline assembly and load it."""

class TensorIndices(Sequence):
    r"""
    A structure that can be used to represent the "shape" of a tensor, along with a list of abstract indices.
    This has an optional name, and accompanying symbolica expressions that are considered as additional non-indexed arguments.
    The structure is essentially a list of `Slots` that are used to define the structure of the tensor.
    """

    def __new__(cls,name:Expression,*additional_args:Slot|Expression) -> TensorIndices:
        r"""
        Create a new tensor structure with the given name and slots. Any additional expressions are also passed along.
        """

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...

    def to_expression(self) -> Expression:
        r"""
        Return the symbolica expression of the tensor indices.
        """

    def __len__(self) -> int:
        r"""
        Return the size of the tensor.
        """

    @overload
    def __getitem__(self, idx: int) -> List[int]:
        r"""
        Get the indices of the slot at the given flat index.
        """

    @overload
    def __getitem__(self, s: slice) -> Sequence[List[int]]:
        r"""
        Get the list of expanded indices of the slot at the given slice of flat index.
        """

    @overload
    def __getitem__(self, key: List[int]) -> int:
        r"""
        Get the flattened index of the given indices.
        """

class TensorNetwork:
    r"""
    A tensor network.

    This class is a wrapper around the `TensorNetwork` class from the `spenso` crate.
    Such a network is a graph representing the arithmetic operations between tensors.
    In the most basic case, edges represent the contraction of indices.

    Examples
    --------

    >>> from symbolica_community.tensors import Representation, TensorNetwork
    >>> from symbolica_community import S
    >>> mink = Representation("mink",4)
    >>> bis = Representation("bis",4)
    >>> [mu,nu,i,j,k]=[a.to_expression() for a in  [mink("mu"),mink("nu"),bis("i"),bis("j"),bis("k")]]
    >>> gamma,p,w,mq,id = S("γ","P","W","mq","id")
    >>> expr = gamma(mu,i,k)*(p(2,nu)*gamma(nu,k,j)+mq*id(k,j))*w(1,i)*w(3,mu)
    >>> tn = TensorNetwork(expr)
    >>> print(tn)
    """
    def __new__(cls,expr:Expression) -> TensorNetwork:
        r"""
        Create a new tensor network.
        """

    def contract(self) -> None:
        r"""
        Contract the tensor network.
        """

    def result(self)->Tensor:
        r"""
        Return the result of the contraction. This is only valid after the network has been contracted.
        """

    def __str__(self) -> str:
        ...

class TensorStructure:
    r"""
    A structure that can be used to represent the "shape" of a tensor.
    This has an optional name, and accompanying symbolica expressions that are considered as additional non-indexed arguments.
    The structure is essentially a list of `Representation` that are used to define the structure of the tensor.
    """

    def __new__(cls,*additional_args:Representation|Expression,name:Optional[Expression]=None) -> TensorStructure:
        r"""
        Create a new tensor structure with the given name and representations. Any additional expressions are also passed along.
        """

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...

    def __len__(self) -> int:
        r"""
        Return the size of the tensor.
        """

    @overload
    def __getitem__(self, idx: int) -> List[int]:
        r"""
        Get the indices of the slot at the given flat index.
        """

    @overload
    def __getitem__(self, s: slice) -> Sequence[List[int]]:
        r"""
        Get the list of expanded indices of the slot at the given slice of flat index.
        """

    @overload
    def __getitem__(self, key: List[int]) -> int:
        r"""
        Get the flattened index of the given indices.
        """



def register(tensor:Tensor):
    r"""
    Register the tensor in the tensor registry. The tensor must have at least a name.
    """

def dense(structure:List[int]|List[Slot]|List[Representation]|TensorIndices|TensorStructure,data:List[float]|List[Expression]) -> Tensor:
    r"""
    Create a new dense tensor with the given structure and data.
    The structure can be a list of integers, a list of representations, or a list of slots.
    In the first two cases, no "indices" are assumed, and thus the tensor is indexless (i.e.) it has a shape but no proper way to contract it.
    The structure can also be a proper `TensorIndices` object or `TensorStructure` object.

    The data is either a list of floats or a list of symbolica expressions, of length equal to the number of elements in the structure, in row-major order.
    """
    ...

def sparse_empty(structure:List[int]|List[Slot]|List[Representation]|TensorIndices|TensorStructure,type_info:type) -> Tensor:
    r"""
    Create a new sparse empty tensor with the given structure and type.
    The structure can be a list of integers, a list of representations, or a list of slots.
    In the first two cases, no "indices" are assumed, and thus the tensor is indexless (i.e.) it has a shape but no proper way to contract it.
    The structure can also be a proper `TensorIndices` object or `TensorStructure` object.

    The type is either a float or a symbolica expression.
    """
    ...
