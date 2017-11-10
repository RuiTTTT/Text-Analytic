import matplotlib.pyplot as plt
import numpy

def getPresion(tp, fp):
    return tp / (tp + fp)


def getRecall(tp, fn):
    return tp / (tp + fn)


def f1(presion, recall):
    return 2 * presion * recall / (presion + recall)


def getTPR(tp, fn):
    return tp / (tp + fn)


def getFPR(fp, tn):
    return fp / (fp + tn)

def getROCCurve(fpr,tpr):
    plt.plot(fpr,tpr)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    auc = numpy.trapz(tpr, fpr)
    print(auc)
    plt.show()

def getDETCurve(fpr,fnr):
    plt.plot(fpr, fnr)
    plt.xlabel('False Positive Rate (%)')
    plt.ylabel('False Negative Rate (%)')
    #plt.yscale('log')
    #plt.xscale('log')
    plt.xlim([1,50])
    plt.ylim([1,50])
    plt.show()



threshold = [1, 5, 10, 15, 20, 25, 30, 35, 40, 50]
tp = [20, 50, 60, 80, 88, 90, 95, 96, 97, 98]
fn = [80, 50, 40, 20, 12, 10, 5, 4, 3, 2]
fp = [2, 5, 10, 20, 30, 40, 50, 60, 70, 80]
tn = [98, 95, 90, 80, 70, 60, 50, 40, 30, 20]

tpRate = []
fpRate = []
fnRateDET = []
fpRateDET = []
for i in range(10):
    presion = getPresion(tp[i], fp[i])
    recall = getRecall(tp[i], fn[i])
    f = f1(presion, recall)
    print("Threshold {}: Presion: {}, Recall: {}, F1: {}".format(threshold[i], '%.3f' % presion, '%.3f' % recall,
                                                                 '%.3f' % f))
    tpRate.append(getTPR(tp[i], fn[i]))
    fpRate.append(getFPR(fp[i],tn[i]))
    fnRateDET.append((1-getTPR(tp[i], fn[i]))*100)
    fpRateDET.append(getFPR(fp[i],tn[i])*100)

getROCCurve(fpRate,tpRate)
getDETCurve(fpRateDET,fnRateDET)