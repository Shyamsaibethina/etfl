# -*- coding: utf-8 -*-
"""
.. module:: thermome
   :platform: Unix, Windows
   :synopsis: Thermodynamics-based Flux Analysis

.. moduleauthor:: pyTFA team

Constraints declarations

"""


class CatalyticConstraint(ReactionConstraint):
    """
    Class to represent a enzymatic constraint
    """

    prefix = 'EC_'


class ModelConstraint(GenericConstraint):
    """
    Class to represent a variable attached to the model
    """

    def __init__(self, model, expr, id_, **kwargs):
        GenericConstraint.__init__(self,
                                   id_= id_,
                                   expr=expr,
                                   model=model,
                                   **kwargs)


class GeneConstraint(GenericConstraint):
    """
    Class to represent a variable attached to a enzyme
    """

    def __init__(self, gene, expr, **kwargs):
        self.gene = gene
        model = gene.model

        GenericConstraint.__init__(self,
                                   id_=self.id,
                                   expr=expr,
                                   model=model,
                                   **kwargs)

    @property
    def id(self):
        return self.gene.id

    @property
    def model(self):
        return self.gene.model


class EnzymeConstraint(GenericConstraint):
    """
    Class to represent a variable attached to a enzyme
    """

    def __init__(self, enzyme, expr, **kwargs):
        self.enzyme = enzyme
        model = enzyme.model

        GenericConstraint.__init__(self,
                                   id_=self.id,
                                   expr=expr,
                                   model=model,
                                   **kwargs)

    @property
    def id(self):
        return self.enzyme.id

    @property
    def model(self):
        return self.enzyme.model


class MassBalance(EnzymeConstraint):
    """
    Class to represent a enzymatic constraint
    """

    prefix = 'MB_'


class TranslationConstraint(ReactionConstraint):
    """
    Class to represent a Translation constraint
    """

    prefix = 'TR_'


class GrowthCoupling(ReactionConstraint):
    """
    Class to represent a growth capacity constraint
    """

    prefix = 'GC_'


class TotalCapacity(CatalyticConstraint):
    """
    Class to represent the total capacity of constraint of a species, e.g
    Ribosome or RNA
    """

    prefix = 'TC_'


class ExpressionCoupling(GeneConstraint):

    prefix = 'EX'


class RibosomeRatio(ModelConstraint):
    """
    Represents the availability of free ribosomes (non bound)
    R_free = 0.2*R_total
    """

    prefix = 'RR_'


class GrowthChoice(ModelConstraint):
    """
    Class to represent a variable attached to a reaction
    """

    prefix = 'GR_'


class LinearizationConstraint(ModelConstraint):
    """
    Class to represent a variable attached to a reaction
    """
    @staticmethod
    def from_constraints(cons, model):
        return LinearizationConstraint(
            name = cons.name,
            expr = cons.expr,
            model = model,
            ub = cons.ub,
            lb = cons.lb,
        )

    prefix = 'LC_'