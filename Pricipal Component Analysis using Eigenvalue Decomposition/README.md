一、需求背景

  针对我们关注的研究对象，我们通常会观察一系列特征属性，来对我们感兴趣的对象进行分析，因此我们会去收集大量有关的特征属性，属性越多，越有利于我们细致观测以及分析。但是随着属性增多，也会增加后续数据处理的运算量，带来较大的处理负担。例如，我们对一个城市或者一个区域进行研究的时候，会产生几十，甚至上百个数据也不奇怪。我们收集的数据越多，越有利于我们进行更加细致的研究和考察。但是，数据维度过大，无疑会使得问题分析变得复杂。同时，有一个现象，就是样本的特征属性之间还存在着一定的相关性，这也会增加问题处理的复杂性。
	因此，主成分分析（PCA）是一个很好的方法。即利用一组线性无关且维度较低的新特征来代替原始的采样数据。
	主成分分析的目标是，减少研究对象数据维度，简单的来说就是降维，但是在降维过程中尽量减少不可避免的信息损失。
	
二、降维目标

1. 目标数据维度减小，减少特征属性
2. 描述数据的信息损失尽可能少，数据降维一定伴随数据的损失，应当控制尽可能少。

三、PCA主要思路

   既然要降低数据维度，那么能不能直接从数据里面挑一个特征属性，直接去掉呢？答案是不行的。因为特征属性之间是存在耦合关系的，也就是说有的属性之间是存在彼此关联的关系的，如此鲁莽的丢弃特征属性进行分析，会对分析结果产生巨大的影响。
   基于以上现象，思路有两点：
   1. 考虑消除属性之间的关联性（相关性），想办法找一组彼此不相关的新特征来描述数据。
   2. 在找到彼此无关的新特征中，进一步舍弃掉不重要的特征，保留较少的特征，实现数据的降维，尽可能保证信息较少地损失。

四、构造无关新特征



五、实际操作



六、n个特征降维的情况


