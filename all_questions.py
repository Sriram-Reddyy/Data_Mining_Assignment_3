# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative hierarchical clustering constructs clusters incrementally through merging or dividing based on distance metrics, while k-means assigns data points to the nearest cluster center, which may lead to biased outcomes in the presence of outliers."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means exhibits randomness in its initial centroid selection, resulting in varying outcomes, whereas Agglomerative hierarchical clustering is deterministic, yielding consistent results each time it is executed."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "While K-means typically requires less time and memory compared to agglomerative hierarchical clustering, making it one of the most efficient clustering algorithms available, it's worth noting that there are alternative algorithms such as the leader algorithm. These alternatives offer different approaches and may be more suitable for specific datasets or objectives. "

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "Splitting clusters decreases the sum of squared errors because having two centroids for the same dataset leads to a reduction in the distance to the nearest centroids, thus minimizing the overall error."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "The sum of squared errors (SSE) serves as an inverse measure of the cohesion of clusters. Therefore, as SSE decreases, cluster cohesion increases, and conversely, as SSE increases, cluster cohesion decreases."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "For k-means, the sum of squares between(SSB) is the measure of separation of clusters. Therefore SSB increases, seperation increases, vice-versa is also true"

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "k-means is independent for cohesion and seperation that means improving cohesion doesn't necessary improve seperation"

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "The total sum of squares (TSS) is sum of SSE and the between SSB as per the k-means.Also TSS is constant during the k-means clustering process."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "The SSB measures cluster separation, while SSE inversely measures cluster cohesion. Therefore, as cohesion increases, SSE decreases, leading to an increase in separation (SSB)."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "As shown in figure, clusters are too far away from centroid to attract points from other."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Given the proximity of the shaded regions in the figure, the clusters will likely contain points from both of these regions."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The centroid at 12.5 is significantly distant from all points, resulting in all other clusters becoming empty."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "(R^2)*4"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*((a*a) + (b*b) + (c*c))"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "4*((R^2) + ((R/2)^2))"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Because there are an equal number of points (100 points) in regions A and B, one centroid will be drawn towards region A. Consequently, the right side of region B (2/3rd portion) will now have two centroids. However, circle C, with a significantly larger number of points (100,000 points), is equally positioned to B. This guarantees the presence of a centroid in circle C due to its stronger pull, even if it was initially absent. The even distribution of points in regions A and B ensures that each region attracts a centroid due to their similar pull."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The centroid will remain at A due to the presence of points in A and the absence of a stronger pull elsewhere. The stronger pull from C will indeed attract one centroid from B. Consequently, all three circles will have one centroid each."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Due to the proximity of circles A and B and their distance from circle C, the points from both A and B will likely be assigned to the centroid in A. Meanwhile, the points in circle C will be distributed between two centroids, each with approximately 50,000 points. As A and B contain the same number of points, the centroid in A will oscillate between the two circles. The centroids in C may move apart slightly, but they will still predominantly remain within C, each containing roughly half of the points."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group A', 'Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Groups A and B can be merged because the rightmost point of A and the leftmost point of B have the smallest single-link distance."

    # type: set
    answers["(b)"] = {'Group A', 'Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Groups A and C can be merged because the rightmost point of A and the farthest point of C have the smallest complete-link distance."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'B', 'C', 'E', 'F', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(a) boundary"] = {'D', 'G'}

    # type: set
    answers["(a) noise"] = {'A', 'H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','D','E','F','G'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'I', 'G', 'J', 'E', 'M', 'B', 'L', 'F', 'D', 'C'}

    # type: set
    answers["(c)-a boundary"] = {'A', 'H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'G', 'I', 'H', 'J', 'E', 'M', 'B', 'D', 'F', 'L', 'C'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 demonstrates the highest entropy because of its more evenly distributed categories."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 exhibits low entropy attributed to its uneven distribution. The overwhelming majority of its data points belong to a single category, resulting in high homogeneity within the cluster." 
    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "The two diagonal entries appear more blue and distinct compared to the other two, suggesting that clusters B and C exhibit higher cohesion than clusters A and D."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The first and third rows correspond to clusters A and C, respectively. This is evident because the colors of the off-diagonal entries for these two rows are all different, indicating varying distances between clusters A (or C) and all other clusters. Specifically, A is closest to C (blue off-diagonal), followed by B (green off-diagonal), and furthest from D (yellow off-diagonal). A similar explanation applies to cluster C. Row 2 corresponds to cluster B, where distances to A and C are the same (green off-diagonal), and the furthest distance from A is indicated by the red entry. Row 4 corresponds to cluster D, where distances from A and C are identical (yellow off-diagonal), but the farthest distance from B is represented by the red off-diagonal entry."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The two diagonal entries appear more blue and distinct compared to the other two, suggesting that two clusters (B and C) have better cohesion than the other two (A and D)."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "1. Rows with less distinct diagonal entries (rows 1 and 4) exhibit all different colors, indicating that all other clusters have distinct distances from these clusters. For instance, Cluster A is closest to B, followed by C, and then D; no two clusters share the same distance to Cluster A.2. Rows with more distinct diagonal entries display two identical colors (besides the diagonal), indicating that these clusters have the same distance to two other clusters and are furthest from one cluster. For example, Cluster B's distance to A and C is similar, but it is furthest from D."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "The two diagonal entries are more blue and distinct compared to the other two, suggesting that two clusters (B and C) have better cohesion than the other two (A and D)."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "All rows exhibit two similar and one different color in their off-diagonal entries. This indicates that each cluster has two other clusters relatively closer to it compared to the remaining one cluster. For example, cluster B is similarly close to clusters A and C compared to cluster D."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "The diagonal entry appears less distinct, indicating that the cluster is less cohesive. Additionally, all off-diagonal entries have different colors, suggesting that all other clusters have varying distances from it (closest to B, followed by C, and furthest from A)."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "The diagonal entry appears more distinct, suggesting that the cluster is cohesive. Additionally, two out of three off-diagonal entries have the same color, indicating that two other clusters (A and C, although the off-diagonal indicating distances with A may be less distinct) are closer to it, while it is the furthest from one other cluster (D)."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "The diagonal entry is more pronounced, suggesting that the cluster is cohesive. Furthermore, two-thirds of the off-diagonal entries have the same color, indicating that two other clusters are closer to it (A and C, despite the off-diagonal indicating distances with A being less distinct), while it is furthest from one other cluster (D)."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "The cluster is closest to A, followed by C, and farthest from B. Its tight-knit nature is demonstrated by the different colors indicating each distance."
    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['Hierarchical', 'Partial', 'Overlapping']

    # type: list
    answers["(b)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: list
    answers["(c)"] = ['Partitional', 'fuzzy', 'complete']


    # type: list
    answers["(d)"] = ['Hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(e)"] = ['Partitional', 'Exclusive', 'Complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Letter grades represent distinct categories that do not overlap (exclusive), with each student receiving only one grade per class (exclusive). Furthermore, all students in the class will receive a grade (complete)."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN can only effectively work for scenario (b) because in this case, the points in the nose, eyes, and mouth are much closer together than the points between these areas. Therefore, DBSCAN could distinguish these areas effectively. However, in scenario (a), the noise is much denser than the interest patterns, causing the nose, eyes, and mouth to be eliminated by DBSCAN."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means can potentially work for scenario (b) if the number of clusters is set to 4, even though the lower density points would also be included. However, K-means is not suitable for scenario (a)."

    # type: string
    answers["(c)"] = "If the reciprocal of density is considered as the next density metric, DBSCAN can be run using this modified density measure."

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
