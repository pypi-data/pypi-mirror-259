import matplotlib.pyplot as plt
from matplotlib import font_manager
from pathlib import Path
import seaborn as sns
import warnings
# 禁用警告
warnings.filterwarnings("ignore")

# 获取包所在的路径
current_PACKAGE_PATH = Path(__file__).resolve().parent


def kde(
        df=None,
        plottype=None,
        xvarname=None,
        yvarname=None,
        groupby=None,
        xlabel=None,
        ylabel=None,
        title=None,
        xlabelsize=12,
        ylabelsize=12,
        titlesize=12,
        xticklabelsize=12,
        yticklabelsize=12,
        xticklabelrotation=0,
        yticklabelrotation=0,
        colormap=None,
        alpha=None,
        fig_length=6.4,
        fig_width=4.8,
        layout="tight",
        hue_order=None,
        order=None,
        fontfamily="华文楷体",
        isshowplot=1,
        savefilename=None,
        snsstyle="darkgrid",
        removeleftspine=0,
        removerightspine=1,
        removetopspine=1,
        removebottomspine=0,
        offset=None,
        trim=0,
        contextstyle="notebook",
        matplotlibstyle=None,
        kdeparamsdict={
            "color": None,
            "isfill": 0,
            "multiple": "layer",
            "iscumulative": 0,
            "bw_adjust": 1,
            "islog": 0,
            "level": 10,
            "thresh": 0.5,
            "islegend": 1,
            "iscommon_norm": 0},
        **kwargs):
    """
    这是一个Seaborn绘指核密度估计图函数的文档字符串。

    参数:
    df (pd.DataFrame object): dataframe。
    xvarname (str): X轴变量名。
    yvarname (str): Y轴变量名。
    groupby (str): 分组变量名。
    xlabel (str): X轴标签。
    ylabel (str): Y轴标签。
    title (str): 图形标题。
    xlabelsize (numeric): X轴标签字体大小。
    ylabelsize (numeric): Y轴标签字体大小。
    titlesize (numeric): 图形标题字体大小。
    xticklabelsize (numeric): X轴刻度标签字体大小。
    yticklabelsize (numeric): Y轴刻度标签字体大小。
    xticklabelrotation (numeric): X轴刻度标签旋转角度。
    yticklabelrotation (numeric): Y轴刻度标签旋转角度。
    colormap (str): 颜色映射名称。
    alpha (numeric): 颜色透明度。
    fig_length (numeric): 图形长度。
    fig_width (numeric): 图形宽度。
    layout (str ; None): 图形在画布上的布局机制{"constrained", "compressed", "tight", None}。
    hue_order (list or array-like): 分组变量的顺序。
    order (list or array-like): 图形主体的顺序。
    fontfamily (str): 支持的中英文字体名称{"方正舒体", "方正姚体", "仿宋", "黑体", "华文彩云", "华文仿宋", "华文琥珀", "华文楷体", "华文隶书", "华文宋体", "华文细黑", "华文新魏", "华文行楷", "华文中宋", "楷体", "隶书", "宋体", "微软雅黑", "新宋体", "幼圆", "TimesNewRoman", "Arial"}。
    isshowplot (binary): 是否显示图形{1,0}。
    savefilename (str): 保存的图形文件名（带后缀）{".pdf", ".png", ".jpg"}。
    snsstyle (str): seaborn绘图风格样式{"darkgrid", "whitegrid", "dark", "white", "ticks"}。
    isremoveleftspine (binary): 是否移除左轴线{1,0}。
    isremoverightspine (binary): 是否移除右轴线{1,0}。
    isremovetopspine (binary): 是否移除上轴线{1,0}。
    isremovebottomspine (binary): 是否移除下轴线{1,0}。
    offset (numeric): 轴线距离图形的距离。
    trim (binary): 是否设置R风格轴线{1,0}。
    contextstyle (str): 图形元素大小风格调整{"paper", "notebook", "talk", "poster"}。
    matplotlibstyle (str): matplotlib支持的绘图风格{"Solarize_Light2", "_classic_test_patch", "_mpl-gallery", "_mpl-gallery-nogrid", "bmh", "classic", "dark_background", "fast", "fivethirtyeight", "ggplot", "grayscale", "seaborn-v0_8", "seaborn-v0_8-bright", "seaborn-v0_8-colorblind", "seaborn-v0_8-dark", "seaborn-v0_8-dark-palette", "seaborn-v0_8-darkgrid", "seaborn-v0_8-deep", "seaborn-v0_8-muted", "seaborn-v0_8-notebook", "seaborn-v0_8-paper", "seaborn-v0_8-pastel", "seaborn-v0_8-poster", "seaborn-v0_8-talk", "seaborn-v0_8-ticks", "seaborn-v0_8-white", "seaborn-v0_8-whitegrid", "tableau-colorblind10"}。
    kdeparamsdict (dict): 控制核密度估计曲线的参数。
    {
        color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 核密度曲线的颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        isfill (binary): 是否填充颜色{1,0}。
        multiple (str): 分组情况下的核密度曲线排列方式{"layer", "stack", "fill"}。
        iscumulative (binary): 是否估计累积分布函数{1,0}。
        bw_adjust (numeric): 窗宽。
        islog (binary or positive numeric): 是否对数化(以10为底)后再绘制箱线图{1,0}或者是对数的底数。
        level (numeric): 等高线等值水平线的数量。
        thresh (numeric): 等值线之间最低比例。
        islegend (binary): 是否显示图例{1,0}。
        iscommon_norm (binary): 分组情况下是否将总数作为计算核密度曲线的方式{1,0}。
    }
    

    返回值：
    Axes对象或者是Axes构成的二维数组

    示例：
    ===============================================================================0
    导入模块
    >>> from TidySeaborn import TidySeabornFlexible
    >>> import matplotlib.pyplot as plt
    >>> from TidySeaborn import GetSeabornData
    >>> import numpy as np
    >>> iris = GetSeabornData("iris")
    >>> tips = GetSeabornData("tips")
    >>> penguins = GetSeabornData("penguins")
    >>> planets = GetSeabornData("planets")
    >>> flights = GetSeabornData("flights")
    >>> titanic = GetSeabornData("titanic")
    >>> diamonds = GetSeabornData("diamonds")
    >>> geyser = GetSeabornData("geyser")
    >>> fmri = GetSeabornData("fmri")
    >>> mpg = GetSeabornData("mpg")
    >>> glue = GetSeabornData("glue")
    ===============================================================================82
    测试核密度估计参数
    ===============================================================================83
    竖直密度估计图
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================84
    水平密度估计图
    >>> ax = TidySeabornFlexible(tips, "kde", yvarname="total_bill", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================85
    整个dataframe绘制多个数据
    >>> ax = TidySeabornFlexible(iris, "kde", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(plottype="kde", xvarname=iris["sepal_length"], block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================86
    调整窗宽
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", kdeparamsdict={"bw_adjust": 0.5}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================87
    分组核密度估计
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================88
    分组排列方式
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 1, "multiple": "stack"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 1, "multiple": "fill"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 1, "multiple": "layer"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================89
    填充颜色
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 1, "multiple": "fill", "isfill": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 1, "multiple": "stack", "isfill": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================90
    累积概率分布
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 0, "multiple": "layer", "isfill": 1, "iscumulative": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================91
    对数处理
    >>> ax = TidySeabornFlexible(diamonds, "kde", xvarname="price", kdeparamsdict={"islog": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================92
    等高线图（二维核密度估计）
    >>> ax = TidySeabornFlexible(geyser, "kde", xvarname="waiting", yvarname="duration", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(geyser, "kde", xvarname="waiting", yvarname="duration", groupby="kind", kdeparamsdict={"isfill": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(geyser, "kde", xvarname="waiting", yvarname="duration", groupby="kind", kdeparamsdict={"isfill": 1, "level": 15, "thresh": 0.4}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================93
    不显示图例
    >>> ax = TidySeabornFlexible(iris, "kde", xvarname="sepal_length", groupby="species", kdeparamsdict={"islegend": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================94
    测试一般绘图的标签参数
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================95
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================96
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/核密度估计图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================97
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================98
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================99
    """
    # 字体对应
    fontfamily_dic = {
        "方正舒体": "FZSTK.TTF",
        "方正姚体": "FZYTK.TTF",
        "仿宋": "simfang.ttf",
        "黑体": "simhei.ttf",
        "华文彩云": "STCAIYUN.TTF",
        "华文仿宋": "STFANGSO.TTF",
        "华文琥珀": "STHUPO.TTF",
        "华文楷体": "STKAITI.TTF",
        "华文隶书": "STLITI.TTF",
        "华文宋体": "STSONG.TTF",
        "华文细黑": "STXIHEI.TTF",
        "华文新魏": "STXINWEI.TTF",
        "华文行楷": "STXINGKA.TTF",
        "华文中宋": "STZHONGS.TTF",
        "楷体": "simkai.ttf",
        "隶书": "SIMLI.TTF",
        "宋体": "simsun.ttc",
        "微软雅黑": "msyhl.ttc",
        "新宋体": "simsun.ttc",
        "幼圆": "SIMYOU.TTF",
        "TimesNewRoman": "times.ttf",
        "Arial": "arial.ttf"
    }
    # 设置字体路径
    fontpath = Path(
        current_PACKAGE_PATH, "fonts/{}".format(fontfamily_dic[fontfamily]))
    fontobj = font_manager.FontProperties(fname=fontpath)
    # 默认的字典
    kdeparamsdictdefault = {
        "color": None,
        "isfill": 0,
        "multiple": "layer",
        "iscumulative": 0,
        "bw_adjust": 1,
        "islog": 0,
        "level": 10,
        "thresh": 0.5,
        "islegend": 1,
        "iscommon_norm": 0}
    # 更新字典
    kdeparamsdictdefault.update(kdeparamsdict)
    if matplotlibstyle is None:
        with sns.axes_style(snsstyle):
            sns.set_context(contextstyle)
            # 开始绘图，画布参数
            fig, ax = plt.subplots(
                figsize=(fig_length, fig_width), layout=layout)
            # 核心变量参数，颜色参数，图形参数
            sns.kdeplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                        hue_order=hue_order, color=kdeparamsdictdefault["color"],
                        fill=bool(kdeparamsdictdefault["isfill"]), multiple=kdeparamsdictdefault["multiple"],
                        cumulative=bool(kdeparamsdictdefault["iscumulative"]), bw_adjust=kdeparamsdictdefault["bw_adjust"],
                        log_scale=bool(kdeparamsdictdefault["islog"]) if kdeparamsdictdefault[
                            "islog"] == 0 or kdeparamsdictdefault["islog"] == 1 else kdeparamsdictdefault["islog"],
                        levels=kdeparamsdictdefault["level"], thresh=kdeparamsdictdefault["thresh"],
                        legend=bool(kdeparamsdictdefault["islegend"]), common_norm=bool(kdeparamsdictdefault["iscommon_norm"])
                        )
    else:
        with plt.style.context(matplotlibstyle):
            # 开始绘图，画布参数
            fig, ax = plt.subplots(
                figsize=(fig_length, fig_width), layout=layout)
            # 核心变量参数，颜色参数，图形参数
            sns.kdeplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                        hue_order=hue_order, color=kdeparamsdictdefault["color"],
                        fill=bool(kdeparamsdictdefault["isfill"]), multiple=kdeparamsdictdefault["multiple"],
                        cumulative=bool(kdeparamsdictdefault["iscumulative"]), bw_adjust=kdeparamsdictdefault["bw_adjust"],
                        log_scale=bool(kdeparamsdictdefault["islog"]) if kdeparamsdictdefault[
                            "islog"] == 0 or kdeparamsdictdefault["islog"] == 1 else kdeparamsdictdefault["islog"],
                        levels=kdeparamsdictdefault["level"], thresh=kdeparamsdictdefault["thresh"],
                        legend=bool(kdeparamsdictdefault["islegend"]), common_norm=bool(kdeparamsdictdefault["iscommon_norm"])
                        )
    # 标题参数
    if xlabel is not None:
        ax.set_xlabel(xlabel, fontproperties=fontobj,
                        fontsize=xlabelsize)
    if ylabel is not None:
        ax.set_ylabel(ylabel, fontproperties=fontobj,
                        fontsize=ylabelsize)
    if title is not None:
        ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
    # 刻度参数，刻度标签参数
    ax.tick_params('x', labelsize=xticklabelsize,
                    rotation=xticklabelrotation)
    ax.tick_params('y', labelsize=yticklabelsize,
                    rotation=yticklabelrotation)
    ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                    fontproperties=fontobj)
    ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                    fontproperties=fontobj)
    # 移除spines
    sns.despine(
        left=removeleftspine,
        right=removerightspine,
        top=removetopspine,
        bottom=removebottomspine,
        offset=offset,
        trim=trim)
    if savefilename is not None:
        fig.savefig(savefilename)
    else:
        pass
    if bool(isshowplot):
        plt.show(**kwargs)
    else:
        pass
    return ax
