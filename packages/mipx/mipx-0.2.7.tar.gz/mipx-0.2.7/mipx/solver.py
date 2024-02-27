# -*- coding: utf-8 -*-
# @Time    : 2023/3/31 22:04
# @Author  : luyi
from typing import Generator, List, Literal, Union, Tuple, Dict

from ortools.linear_solver import pywraplp
try:
    from ortools.linear_solver.linear_solver_natural_api import OFFSET_KEY  # type: ignore
except Exception as e:
    from ortools.linear_solver.python.linear_solver_natural_api import CastToLinExp, OFFSET_KEY
from ortools.sat.python import cp_model

from .cplexcpsolver import CplexCpSolver

from .cplexmpsolver import CplexMpSolver
from .constants import Vtype, ObjType, OptimizationStatus, CmpType, Params
from .interface_ import IModel, IVar, ITupledict
from .tupledict import tupledict
from .utilx import is_list_or_tuple, get_combinations, name_str, \
    is_generator, check_bool_var, is_bool_var, pre_condition
from .variable import IntervalVar
from .cpsolver import CpModelSolver

INFINITY = float("inf")
INFINITY_CP = cp_model.INT32_MAX
Real = Union[float, int]


class LinearConstraint(pywraplp.LinearConstraint):
    """
    线性约束

    Args:
        pywraplp (_type_): 线性
    """

    def __init__(self, expr, lb, ub):
        self.__expr = expr
        self.__lb = lb
        self.__ub = ub
        super().__init__(expr, lb, ub)

    def lbAndUb(self) -> Tuple[float, float]:
        coeffs = self.__expr.GetCoeffs()
        constant = coeffs.pop(OFFSET_KEY, 0.0)
        lb = -INFINITY
        ub = INFINITY
        if self.__lb > -INFINITY:
            lb = self.__lb - constant
        if self.__ub < INFINITY:
            ub = self.__ub - constant
        return lb, ub

    def linear_expr(self) -> pywraplp.LinearExpr:
        return self.__expr


class Model:
    """模型接口"""

    def __init__(self, solver_id: Literal["SCIP", "CBC", "CP", "SAT", "CLP", "CPLEX", "CPLEX_CP"] = "SCIP", name=""):
        super().__init__()
        self.solver_id = solver_id
        if solver_id == "CP":
            self.__model = CpModelSolver(name=name)
        elif solver_id == 'CPLEX':
            self.__model = CplexMpSolver(name=name)
        elif solver_id == 'CPLEX_CP':
            self.__model = CplexCpSolver(name=name)
        else:
            self.__model = ModelSolver(solver_id=solver_id, name=name)
        self._is_cp = solver_id == "CP"

    @property
    def Params(self) -> Params:
        return self.__model.Params

    @property
    def Infinity(self) -> float:
        return self.__model.Infinity

    # -> Any | _SumArray | LinearExpr | ZeroExpr | SumArray | None:

    def Sum(self, expr_array):
        return self.__model.Sum(expr_array)

    def setHint(self, start: Dict[IVar, Real]):
        self.__model.setHint(start)  # type: ignore

    def setTimeLimit(self, time_limit_seconds: int):
        """
        设置程序最大运行时间
        :param time_limit_seconds: 秒
        """
        self.__model.setTimeLimit(time_limit_seconds)

    def wall_time(self) -> float:
        """
        求解所花费的时间
        :return: 求解所花费的时间，单位毫秒
        """
        return self.__model.wall_time()

    def iterations(self):
        """

        :return: 算法迭代的次数
        """
        return self.__model.iterations()

    def nodes(self) -> Real:
        """

        :return: 节点数
        """
        return self.__model.nodes()

    def addVar(self, lb=0, ub=None,
               vtype: Vtype = Vtype.CONTINUOUS, name: str = "") -> IVar:
        """
        创建变量
        :param lb: 变量下界
        :param ub: 变量上界
        :param vtype: 变量类型： Vtype.CONTINUOUS（连续）,Vtype.BINARY(0-1变量), Vtype.BINARY（整数变量）
        :param name:变量名
        :return:变量实体
        """
        lb, ub = self._get_update_lub(lb, ub, vtype)
        return self.__model.addVar(lb=lb, ub=ub, vtype=vtype, name=name)

    def _get_update_lub(self, lb, ub, vtype: Vtype):
        if self._is_cp and ub is None:
            ub = INFINITY_CP
        elif ub is None:
            ub = INFINITY
        if self.solver_id in ['SAT', 'CBC']:
            ub = INFINITY_CP if ub == INFINITY else ub
        if vtype == Vtype.BINARY:
            if ub > 0 or ub is None:
                ub = 1
            if lb > 0:
                lb = 1
            if lb > ub:
                raise Exception("0-1变量lb>=ub")
        return lb, ub

    def addVars(self, *indices, lb: Real = 0, ub=None,
                vtype: Vtype = Vtype.CONTINUOUS, name: str = "") -> ITupledict:
        """
        创建多维变量
        :param indices:多维的参数，如addVars(1,2),addVars(mList,nList),addVars([1,2,3],[3,4,5])等。
        :param lb:变量下界
        :param ub:变量上界
        :param vtype:变量类型： Vtype.CONTINUOUS（连续）,Vtype.BINARY(0-1变量), Vtype.BINARY（整数变量）
        :param name:变量名
        :return:tupledict类型
        """
        pre_condition(len(indices) > 0, 'addVars中多维参数缺失')
        lb, ub = self._get_update_lub(lb, ub, vtype)
        return self.__model.addVars(*indices, lb=lb, ub=ub, vtype=vtype, name=name)

    def getVars(self) -> List[IVar]:
        """
        获取所有的变量对象
        :return:
        """
        return self.__model.getVars()

    def getVar(self, i) -> IVar:
        """
        获取第i个变量
        :param i:
        :return:
        """
        return self.__model.getVar(i)

    def addConstr(self, lin_expr, name=""):
        """
        向模型添加约束条件，
        :param lin_expr:线性约束表达式
        :param name: 约束名称
        :return:
        """
        return self.__model.addConstr(lin_expr, name=name)

    def addConstrs(self, lin_exprs: List | Generator | Tuple, name=""):
        """
        向模型添加多个约束条件，
        :param lin_exprs: 线性约束表达式集合 可以为列表或者元组。
        :param name:名称
        :return:
        """
        return self.__model.addConstrs(lin_exprs, name=name)

    def setObjective(self, expr):
        """
        设置模型的单一目标
        :param expr: 目标表达式
         优化方向。ObjType.MINIMIZE（最小值），ObjType.MAXIMIZE(最大值)
        :return:
        """
        self.__model.setObjective(expr)

    def setObjectiveN(self, expr, index: int, priority: int = 0, weight: float = 1, name: str = ""):
        """
         多目标优化，优化最小值
        :param expr: 表达式
        :param index: 目标函数对应的序号 (默认 0，1，2，…), 以 index=0 作为目标函数的值, 其余值需要另外设置参数
        :param priority: 分层序列法多目标决策优先级(整数值), 值越大优先级越高【未实现】
        :param weight: 线性加权多目标决策权重(在优先级相同时发挥作用)
        :param name: 名称
        :return:
        """
        self.__model.setObjectiveN(
            expr, index, priority=priority, weight=weight, name=name)

    def addGenConstrAnd(self, resvar, varList: List[IVar], name=""):
        """
        and 运算。
        addGenConstrAnd(y, [x1, x2]) 表示y = max(x1,x2)。 所有变量均为0-1变量
        :param resvar:
        :param varList:
        :param name:
        :return:
        """
        self.__model.addGenConstrAnd(resvar, varList, name=name)

    def addGenConstrOr(self, resvar: IVar, varList: List[IVar], name=""):
        """
        或运算
        addGenConstrOr(y, [x1, x2]) 表示y = min(x1,x2)。 所有变量均为0-1变量
        :param resvar:
        :param varList:
        :param name:
        :return:
        """
        self.__model.addGenConstrOr(resvar, varList, name=name)

    def addGenConstrXOr(self, resvar: IVar, varList: List[IVar], name=""):
        """
        异或运算
        addGenConstrXOr(y, [x1, x2])。 所有变量均为0-1变量
        :param resvar:
        :param varList:
        :param name:
        :return:
        """
        self.__model.addGenConstrXOr(resvar, varList, name=name)

    def addGenConstrPWL(self, var_y, var_x, x, y, name=""):
        """
       设置分段约束
       参考gurobi
        model.setPWLObj(var, [1, 3, 5], [1, 2, 4])
       :param var_y: f(x)
       :param var_x:指定变量的目标函数是分段线性
       :param x:  定义分段线性目标函数的点的横坐标值(非减序列)
       :param y:定义分段线性目标函数的点的纵坐标值
       :return:
       """
        self.__model.addGenConstrPWL(var_y, var_x, x, y, name=name)

    def addGenConstrIndicator(self, binvar: IVar, binval: bool, lhs: IVar, sense: CmpType, rhs, M,
                              name: str = ""):
        """
         若 binvar 为binval ,则 lhs 与 rhs 之间有sense 的关系
        若M不指定，则程序会给与默认。但仍推荐给出M。程序自动给出的可能会存在问题。
        :param binvar: 0-1变量
        :param binval: bool 常量
        :param lhs:  左侧变量
        :param sense: 等号，大于等于，小于等于
        :param rhs: 右侧常量
        :param M: 大M
        :return:
        """
        self.__model.addGenConstrIndicator(
            binvar, binval, lhs, sense, rhs, M=M, name=name)

    def addIndicator(self, binvar: IVar, binval: bool, expr,
                     name: str = ""):
        self.__model.addIndicator(binvar, binval, expr, name)

    def addGenConstrAbs(self, resvar, var_abs: IVar, M, name=""):
        """
        绝对值 resvar = |var_abs|
        :param resvar:
        :param var_abs:
        :param name:
        :return:
        """
        self.__model.addGenConstrAbs(resvar, var_abs, name=name, M=M)

    def addConstrMultiply(self, z: IVar, l: Tuple[IVar, IVar], name=""):
        """
        满足 z = x * y
        其中 x 为0,1变量
        :param l:
        :param z: 变量
        :param name:
        :return:
        """
        self.__model.addConstrMultiply(z, l, name=name)

    def addRange(self, expr, min_value: Union[float, int], max_value: Union[float, int], name=""):
        """
         添加范围约束
        :param expr: 表达式
        :param min_value: 最小值
        :param max_value: 最大值
        :param name:名称
        :return:
        """
        self.__model.addRange(expr, min_value, max_value, name=name)

    def addConstrOr(self, constrs: List, ok_num: int = 1, cmpType: CmpType = CmpType.EQUAL, name: str = "", M=None):
        """
         约束的满足情况,满足的次数
        :param constr: 所有的约束
        :param ok_num:  需要满足的个数，具体则根据cmpType
        :param cmpType: CmpType.LESS_EQUAL CmpType.EQUAL,CmpType.GREATER_EQUAL
        :param name: 名称
        :param M: M值，推荐指定M值。
        :return:
        """
        self.__model.addConstrOr(
            constrs, ok_num=ok_num, cmpType=cmpType, name=name, M=M)

    def addKpi(self, kpi_arg, name=None) -> IVar:
        return self.__model.addKpi(kpi_arg, name)

    def numVars(self) -> int:
        """
        变量个数
        :return:
        """
        return self.__model.numVars()

    def numConstraints(self) -> int:
        """
        约束个数
        :return:
        """
        return self.__model.numConstraints()

    def write(self, filename: str, obfuscated=False):
        """
       写入到文件
       :param filename:文件名，支持后缀 .lp .mps .proto(目前有问题)
       :param obfuscated: 是否混淆，默认不混淆
       :return:
       """
        self.__model.write(filename, obfuscated=obfuscated)

    def read(self, path: str):
        self.__model.read(path)

    @property
    def ObjVal(self) -> Real:
        """目标值"""
        return self.__model.ObjVal

    def optimize(self, obj_type: ObjType = ObjType.MINIMIZE) -> OptimizationStatus:
        """
        优化目标
        :param time_limit_milliseconds:最大运行时长
        :param obj_type:优化目标。ObjType.MINIMIZE（最小值），ObjType.MAXIMIZE(最大值)
        :param enable_output: 是否显示gap日志。
        :return:
        """
        return self.__model.optimize(obj_type=obj_type)

    def clear(self):
        self.__model.clear()

    def close(self):
        self.__model.close()

    def valueExpression(self, expression):
        """
        计算表达式的值。
        :param expression:
        :return:
        """
        return self.__model.valueExpression(expression)

    def newIntervalVar(self, start, size, end, name=""):
        """
        创建变量： start+size=end

        Args:
            start (_type_): 开始
            size (_type_): 大小
            end (_type_): 结束
            name (str, optional): 名称. Defaults to "".
        """
        return self.__model.newIntervalVar(start, size, end, name=name)

    def addNoOverlap(self, interval_vars: List, M: int):
        """
        互相之间不重复

        Args:
            interval_vars (List): 间隔变量
        """
        self.__model.addNoOverlap(interval_vars, M)

    def setNumThreads(self, num_theads: int):
        """
        设置线程的个数

        Args:
            num_theads (int): 线程个数
        """
        self.__model.setNumThreads(num_theads)


class ModelSolver(IModel):
    """
    模型
    """

    def __init__(self, solver_id="SCIP", name=""):
        """
            solver_id is case insensitive, and the following names are supported:
              - CLP_LINEAR_PROGRAMMING or y
              - CBC_MIXED_INTEGER_PROGRAMMING or CBC
              - GLOP_LINEAR_PROGRAMMING or GLOP
              - BOP_INTEGER_PROGRAMMING or BOP
              - SAT_INTEGER_PROGRAMMING or SAT or CP_SAT
              - SCIP_MIXED_INTEGER_PROGRAMMING or SCIP
              - GUROBI_LINEAR_PROGRAMMING or GUROBI_LP
              - GUROBI_MIXED_INTEGER_PROGRAMMING or GUROBI or GUROBI_MIP
              - CPLEX_LINEAR_PROGRAMMING or CPLEX_LP
              - CPLEX_MIXED_INTEGER_PROGRAMMING or CPLEX or CPLEX_MIP
              - XPRESS_LINEAR_PROGRAMMING or XPRESS_LP
              - XPRESS_MIXED_INTEGER_PROGRAMMING or XPRESS or XPRESS_MIP
              - GLPK_LINEAR_PROGRAMMING or GLPK_LP
              - GLPK_MIXED_INTEGER_PROGRAMMING or GLPK or GLPK_MIP
            """
        super().__init__(solver_id)
        self.name = name
        self.__solver: pywraplp.Solver = pywraplp.Solver.CreateSolver(
            solver_id)
        self._flag_objective_n = False
        self._flag_objective = False

    @property
    def Infinity(self) -> float:
        return INFINITY

    @staticmethod
    def Sum(expr_array):
        result = pywraplp.SumArray(expr_array)
        return result

    def setHint(self, start: Dict[IVar, Real]):
        _vars = []
        _values = []
        for var, value in start.items():
            _vars.append(var)
            _values.append(value)
        self.__solver.SetHint(_vars, _values)

    def setTimeLimit(self, time_limit_seconds):
        self.__solver.set_time_limit(time_limit_seconds * 1000)

    def wall_time(self) -> int:
        """
        求解所花费的时间 milliseconds
        :return:
        """
        return self.__solver.wall_time()

    def iterations(self) -> int:
        """迭代次数"""
        return self.__solver.iterations()

    def nodes(self) -> int:
        return self.__solver.nodes()

    def addVar(self, lb: Real = 0.0, ub: Real = INFINITY,
               vtype: Vtype = Vtype.CONTINUOUS, name: str = "") -> IVar:
        """
            Add a decision variable to a model.
        :param lb: Lower bound for new variable.
        :param ub: Upper bound for new variable.
        :param vtype: variable type for new variable(Vtype.CONTINUOUS, Vtype.BINARY, Vtype.INTEGER).
        :param name: Name for new variable.write
        :return: variable.
        """
        if vtype == Vtype.CONTINUOUS:
            var: IVar = self.__solver.NumVar(lb, ub, name)
        elif vtype == Vtype.INTEGER:
            var: IVar = self.__solver.IntVar(lb, ub, name)
        elif vtype == Vtype.BINARY:
            var: IVar = self.__solver.IntVar(lb, ub, name)
        var.v_type = vtype  # type: ignore
        var._solver = self.__solver  # type: ignore
        return var

    def addVars(self, *indices, lb: Real = 0.0, ub: Real = INFINITY,
                vtype: Vtype = Vtype.CONTINUOUS, name: str = "") -> ITupledict:
        li = []
        for ind in indices:
            if isinstance(ind, int):
                ind = [i for i in range(ind)]
            elif is_list_or_tuple(ind):
                pass
            elif isinstance(ind, str):
                ind = [ind]
            else:
                raise ValueError("error input")
            li.append(ind)
        all_keys_tuple = get_combinations(li)
        tu_dict = tupledict(
            [[key, self.addVar(lb, ub, vtype, name_str(name, key))] for key in all_keys_tuple])
        return tu_dict

    def getVars(self) -> List[IVar]:
        """
        Retrieve a list of all variables in the model.
        :return: All variables in the model.
        """
        return self.__solver.variables()

    def getVar(self, i) -> IVar:
        """
        获得第i个变量
        :param i:
        :return:
        """
        return self.__solver.variable(i)

    def addConstr(self, lin_expr, name="") -> LinearConstraint:
        return self.__solver.Add(lin_expr, name)

    def addConstrs(self, lin_exprs, name=""):
        if not is_list_or_tuple(lin_exprs) and not is_generator(lin_exprs):
            raise RuntimeError("constraint conditions are not a set or list")
        for i, lin_expr in enumerate(lin_exprs):
            self.addConstr(lin_expr, name_str(name, i))

    def setObjective(self, expr):
        """
        Set the model objective equal to a linear expression
        :param expr:New objective expression
        :param obj_type:Optimization sense (Sense.MINIMIZE for minimization, Sense.MAXIMIZE for maximization)
        """
        self._flag_objective = True
        if self._flag_objective_n:
            raise RuntimeError(
                "setObjective and setObjectiveN can only be used for one of them")
        self.__solver.Minimize(expr)

    def _set_objective_sense(self, obj_type: ObjType):
        if obj_type == ObjType.MINIMIZE:
            self.__solver.Objective().SetMinimization()
        else:
            self.__solver.Objective().SetMaximization()

    def setObjectiveN(self, expr, index: int, priority: int = 0, weight: float = 1, name: str = ""):
        """
        多目标优化，优化最小值
        :param name:
        :param expr: 表达式
        :param index: 目标函数对应的序号 (默认 0，1，2，…), 以 index=0 作为目标函数的值, 其余值需要另外设置参数
        :param priority:分层序列法多目标决策优先级(整数值), 值越大优先级越高,# 未实现。
        :param weight: 线性加权多目标决策权重(在优先级相同时发挥作用)
        """
        self._flag_objective_n = True
        if self._flag_objective:
            raise RuntimeError(
                "setObjective and setObjectiveN can only be used for one of them")
        objective: pywraplp.Objective = self.__solver.Objective()
        if isinstance(expr, Real):
            objective.SetOffset(expr)
        else:
            coeffs = expr.GetCoeffs()
            objective.SetOffset(coeffs.pop(OFFSET_KEY, 0.0))
            for v, c, in list(coeffs.items()):
                objective.SetCoefficient(v, float(c) * weight)

    def addGenConstrAnd(self, resvar, varList: List[IVar], name=""):
        """
        和 addGenConstrAnd(y, [x1,x2])
        :param resvar:
        :param varList:
        :param name:
        :return:
        """
        check_bool_var(resvar, varList)
        for var in varList:
            self.addConstr(resvar <= var)
        self.addConstr(resvar >= self.Sum(varList) - len(varList) + 1)

    def addGenConstrOr(self, resvar: IVar, varList: List[IVar], name=""):
        """
        或
        :param resvar:
        :param varList:
        :param name:
        :return:
        """
        check_bool_var(resvar, varList)
        for var in varList:
            self.addConstr(resvar >= var)
        self.addConstr(resvar <= self.Sum(varList))

    def addGenConstrXOr(self, resvar: IVar, varList: List[IVar], name=""):
        """
        异或
        :param resvar:
        :param varList:
        :param name:
        :return:
        """
        if len(varList) != 2:
            raise ValueError("length of vars must be 2")
        check_bool_var(resvar, varList)
        self.addConstr(resvar >= varList[0] - varList[1])
        self.addConstr(resvar >= varList[1] - varList[0])
        self.addConstr(resvar <= varList[0] + varList[1])
        self.addConstr(resvar <= 2 - varList[0] - varList[1])

    def addGenConstrPWL(self, var_y, var_x, x, y, name=""):
        """
        设置分段约束
        参考gurobi
         model.setPWLObj(var, [1, 3, 5], [1, 2, 4])
        :param var_y: f(x)
        :param var_x:指定变量的目标函数是分段线性
        :param x:  定义分段线性目标函数的点的横坐标值(非减序列)
        :param y:定义分段线性目标函数的点的纵坐标值
        :return:
        """

        pass

    def addGenConstrIndicator(self, binvar: IVar, binval: bool, lhs: IVar, sense: CmpType, rhs: float, M: float,
                              name: str = ""):
        """
         若 binvar 为binval ,则 lhs 与 rhs 之间有sense 的关系

        :param binvar: 0-1变量
        :param binval: bool 常量
        :param lhs:  左侧变量
        :param sense: 等号，大于等于，小于等于
        :param rhs: 右侧常量
        :param M: 大M
        :return:
        """
        if M is None:
            M = abs(rhs) + 100  # TODO:待优化
        if binval is True:
            z = 1 - binvar
        else:
            z = binvar
        if sense == CmpType.GREATER_EQUAL:
            self.addConstr(lhs + M * z >= rhs)
        elif sense == CmpType.EQUAL:
            self.addConstr(lhs + M * z >= rhs)
            self.addConstr(lhs - M * z <= rhs)
        else:
            self.addConstr(lhs - M * z <= rhs)

    def addIndicator(self, binvar: IVar, binval: bool, expr,
                     name: str = ""):
        raise RuntimeError("not implemented")

    def addGenConstrAbs(self, resvar, var_abs: IVar, name="", M=None):
        x = self.addVars(2, name='')
        _M = 10000000
        if M is not None:
            _M = M
        self.addConstr(var_abs == x[0] - x[1])
        self.addConstr(resvar == x[0] + x[1])
        y = self.addVar(vtype=Vtype.BINARY)
        # x[0] * x[1]==0 的约束
        self.addConstr(x[0] <= y * _M)
        self.addConstr(x[1] <= (1 - y) * _M)

    def addConstrMultiply(self, z: IVar, l: Tuple[IVar, IVar], name=""):
        """x * y = z"""
        super().addConstrMultiply(z, l)
        x = l[0]
        y = l[1]
        if not is_bool_var(x) and not is_bool_var(y):
            raise RuntimeError("At least one binary variable is required.")
        if is_bool_var(y):
            x, y = y, x
        M = y.Ub
        if self.solver_id in ['SAT', 'CBC']:
            M = INFINITY_CP if M == INFINITY else M
        self.addConstr(z <= y)
        self.addConstr(z <= x * M)
        self.addConstr(z >= y + (x - 1) * M)

    def addRange(self, expr, min_value: Union[float, int], max_value: Union[float, int], name=""):
        """
        添加范围约束
        :param
        expr:
        :param
        min_value:
        :param
        max_value:
        :param
        name:
        :return:
        """
        if isinstance(min_value, int | float) and isinstance(max_value, int | float):
            if min_value > max_value:
                raise ValueError("min_value is bigger than max_value")
        self.addConstr(expr >= min_value)
        self.addConstr(expr <= max_value)

    def addConstrOr(self, constrs: List[pywraplp.LinearConstraint], ok_num: int = 1, cmpType: CmpType = CmpType.EQUAL, name: str = "", M=None):
        """
            约束的满足情况

        :param constr: 所有的约束
        :param ok_num: 需要满足的个数，具体则根据cmpType
        :param cmpType: CmpType.LESS_EQUAL CmpType.EQUAL,CmpType.GREATER_EQUAL
        :param name: 名称
        :return:
        """
        constr_num = len(constrs)
        x = []
        for i in range(constr_num):
            x.append(self.addVar(vtype=Vtype.BINARY))
            tempConstr = _change_to_linear_constraint(constrs[i])
            lb, ub = tempConstr.lbAndUb()
            expr = tempConstr.linear_expr()
            tempM = 0
            if M is not None:
                tempM = M
            if lb > -INFINITY:  # 若大于
                if M is None:
                    tempM = (abs(lb) + 1) * 10
                self.addConstr(expr + tempM * (1 - x[i]) >= lb)
            if ub < INFINITY:
                if M is None:
                    tempM = (abs(ub) + 1) * 10
                self.addConstr(expr - tempM * (1 - x[i]) <= ub)

        match cmpType:
            case CmpType.EQUAL:
                self.addConstr(self.Sum(x) == ok_num)
            case CmpType.GREATER_EQUAL:
                self.addConstr(self.Sum(x) >= ok_num)
            case CmpType.LESS_EQUAL:
                self.addConstr(self.Sum(x) <= ok_num)

    def addKpi(self, kpi_arg, name=None) -> IVar:
        kpi = self.addVar()
        self.addConstr(kpi == kpi_arg)
        return kpi

    def numVars(self) -> int:
        """
        当前的变量的个数
        :return:
        """
        return self.__solver.NumVariables()

    def numConstraints(self) -> int:
        """
        当前的约束的个数
        :return:
        """
        return self.__solver.NumConstraints()

    def write(self, filename: str, obfuscated=False):
        """
        写入到文件
        :param filename:文件名，支持后缀 .lp .mps .proto
        :param obfuscated:
        :return:
        """
        filename = filename.lower()
        content = ""
        if filename.endswith(".lp"):
            content = self.__solver.ExportModelAsLpFormat(obfuscated=False)
        elif filename.endswith(".mps"):
            content = self.__solver.ExportModelAsMpsFormat(True, obfuscated)
        elif filename.endswith(".proto"):
            raise TypeError(".proto 导出异常，待修复")

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

    def read(self, path: str):
        raise RuntimeError("not implemented")

    def getVarByName(self, name: str) -> IVar:
        return self.__solver.LookupVariable(name)

    @property
    def ObjVal(self):
        return self.__solver.Objective().Value()

    def _set_params(self):
        if self.Params.TimeLimit:
            self.setTimeLimit(self.Params.TimeLimit)
            # 是否允许输出运算信息，包括gap等
        if self.Params.EnableOutput:
            self.__solver.EnableOutput()

    def optimize(self, obj_type: ObjType = ObjType.MINIMIZE) -> OptimizationStatus:
        self._set_params()
        if obj_type is not None:
            self._set_objective_sense(obj_type)
        # GAP 设置。
        params = pywraplp.MPSolverParameters()
        # 配置参数
        if self.Params.MIPGap:
            params.SetDoubleParam(params.RELATIVE_MIP_GAP, self.Params.MIPGap)
        status = self.__solver.Solve(params)

        if status == pywraplp.Solver.OPTIMAL:
            result = OptimizationStatus.OPTIMAL
        elif status == pywraplp.Solver.INFEASIBLE:
            result = OptimizationStatus.INFEASIBLE
        elif status == pywraplp.Solver.UNBOUNDED:
            result = OptimizationStatus.UNBOUNDED
        elif status == pywraplp.Solver.FEASIBLE:
            result = OptimizationStatus.FEASIBLE
        elif status == pywraplp.Solver.NOT_SOLVED:
            result = OptimizationStatus.NO_SOLUTION_FOUND
        else:
            result = OptimizationStatus.ERROR
        return result

    def clear(self):
        self.__solver.Clear()

    def close(self):
        self.clear()
        self.__solver = None  # type: ignore

    def valueExpression(self, expression):
        value = 0
        coeffs = expression.GetCoeffs()
        for key, coeff in coeffs.items():
            if key is OFFSET_KEY:
                value += coeffs.get(key)
            else:
                var: IVar = key
                x = var.X
                value += coeff * x
        return value

    def newIntervalVar(self, start, size, end, name="") -> IntervalVar:
        self.addConstr(start + size == end, name=name)
        return IntervalVar(start, size, end)

    def addNoOverlap(self, interval_vars: List[IntervalVar], M: int):
        m = INFINITY_CP if M is None else M
        for i, var_i in enumerate(interval_vars):
            for j, var_j in enumerate(interval_vars):
                if i == j:
                    continue
                t = self.addVar(vtype=Vtype.BINARY)
                self.addConstr(var_i.start >= var_j.end - (1-t)*m)
                self.addConstr(var_j.start >= var_i.end - t*m)

    def setNumThreads(self, num_theads: int):
        self.__solver.SetNumThreads(num_theads)


def _change_to_linear_constraint(constraint: pywraplp.LinearConstraint) -> LinearConstraint:
    expr = constraint._LinearConstraint__expr  # type: ignore
    ub = constraint._LinearConstraint__ub  # type: ignore
    lb = constraint._LinearConstraint__lb  # type: ignore
    return LinearConstraint(expr, lb, ub)
