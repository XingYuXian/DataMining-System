from sklearn.decomposition import PCA
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture as GMM
from sklearn.metrics import calinski_harabasz_score
from scipy import linalg as lina
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import xlrd
import itertools
from pylab import *
from apyori import apriori
from mlxtend.preprocessing import TransactionEncoder


mpl.rcParams['font.sans-serif'] = ['SimHei']


# rows:行
# cols:列


def Test_cs():
    data_Att = xlrd.open_workbook("cs.xlsx")
    subject = data_Att.sheet_names()
    print(subject)
    table = data_Att.sheet_by_index(0)
    print(table.name, table.nrows, table.ncols)
    data = np.zeros((table.nrows - 1, table.ncols - 2))
    for i in range(table.nrows):
        if i == 0:
            continue
        else:
            data[i - 1] = table.row_values(i)[2:22]

    print(data.shape)
    return data


def Test_pca():
    data_bPca = Test_cs()
    pca = PCA(n_components=2)
    pca.fit(data_bPca)
    c = pca.transform(data_bPca)
    # Sum = np.cumsum(c.explained_variance_ratio_)
    # d = np.argmax(Sum >= 0.7) + 1
    # print(d)
    # plt.plot(Sum)
    # plt.show()
    return c


def Test_Kmeans():
    data_bK = Test_pca()
    cluster_score_CH = np.zeros(9)
    # cluster_score_DBI = np.zeros(9)
    for i in range(2, 10):
        kmean = KMeans(n_clusters=i)
        y = kmean.fit_predict(data_bK)
        cluster_score_CH[i - 2] = calinski_harabasz_score(data_bK, y)
        # cluster_score_DBI[i - 2] = metrics.davies_bouldin_score(data_bK, y)

    d = np.argmax(cluster_score_CH) + 2
    print(d)
    kmean = KMeans(n_clusters=d)
    Y = kmean.fit_predict(data_bK)
    label = kmean.labels_
    num = np.zeros(d + 1)
    for i in range(0, len(label)):
        if label[i] == 1:
            num[1] += 1
        elif label[i] == 2:
            num[2] += 1
        elif label[i] == 3:
            num[3] += 1
        elif label[i] == 4:
            num[4] += 1
        else:
            num[5] += 1
    print(num)
    plt.scatter(data_bK[:, 0], data_bK[:, 1], c=Y)
    plt.show()


def Test_GMM():
    data_bGMM = Test_pca()
    lowest_bic = np.infty
    bic = []
    cv_types = ['spherical', 'tied', 'diag', 'full']
    n_components_range = range(1, 7)
    for cv_type in cv_types:
        for n_components in n_components_range:
            gmm = GMM(n_components=n_components, covariance_type=cv_type)
            gmm.fit(data_bGMM)
            bic.append(gmm.bic(data_bGMM))
            if bic[-1] < lowest_bic:
                lowest_bic = bic[-1]
                best_gmm = gmm
    bic = np.array(bic)
    color_iter = itertools.cycle(['navy', 'turquoise', 'cornflowerblue', 'darkorange'])
    clf = best_gmm
    bars = []
    data_aGMM = best_gmm.predict(data_bGMM)

    # Plot the BIC scores
    plt.figure(figsize=(8, 6))
    spl = plt.subplot(2, 1, 1)
    for i, (cv_type, color) in enumerate(zip(cv_types, color_iter)):
        xpos = np.array(n_components_range) + .2 * (i - 2)
        bars.append(plt.bar(xpos, bic[i * len(n_components_range):
                                      (i + 1) * len(n_components_range)], width=.2, color=color))
    plt.xticks(n_components_range)
    plt.ylim([bic.min() * 1.01 - .01 * bic.max(), bic.max()])
    plt.title('模型BIC分数')
    xpos = np.mod(bic.argmin(), len(n_components_range)) + .65 + \
           .2 * np.floor(bic.argmin() / len(n_components_range))
    plt.text(xpos, bic.min() * 0.97 + .03 * bic.max(), '*', fontsize=14)
    spl.set_xlabel('高斯混合成分个数')
    spl.legend([b[0] for b in bars], cv_types)

    # Plot the winner
    splot = plt.subplot(2, 1, 2)
    Y_ = clf.predict(data_bGMM)
    for i, (mean, cov, color) in enumerate(zip(clf.means_, clf.covariances_, color_iter)):
        if not np.any(Y_ == i):
            continue
        plt.scatter(data_bGMM[Y_ == i, 0], data_bGMM[Y_ == i, 1], .8, color=color)
    plt.xticks(())
    plt.yticks(())
    plt.subplots_adjust(hspace=.35, bottom=.02)
    plt.show()
    return data_aGMM


def Test():
    data_bGMM = Test_pca()
    gmm = GMM(n_components=2)
    gmm.fit(data_bGMM)
    data = gmm.predict(data_bGMM)
    print(data)


def Data_Apriori():
    data = pd.read_excel("cs.xlsx")
    print(data)


def Test_Apriori():
    Data_Apriori()


if __name__ == '__main__':
    Data_Apriori()
