# <a href="http://graphics.stanford.edu/data/3Dscanrep/"> Stanford Bunny </a> ICP

In this repository, the Least Squares Iterative Closest Point (ICP) algorithm with the point-to-plane metric applied to the Stanford Bunny model and outlier data eliminated for more robust allignment. <a href="https://github.com/ReillyBova/Point-Cloud-Registration/tree/master">Point-Cloud-Registration</a> repository mainly used during the implementation process. 
The Stanford Bunny is a ceramic figurine widely used in 3D modeling tasks within computer graphics and vision research. It has been scanned using either the Cyberware 3030 MS scanner or the Stanford Large Statue Scanner, employing laser triangulation to capture spatial coordinates on its surface [3].

For visual comparisons,  both aligned and non-aligned images of the Stanford Bunny are in the "Results" section.

For more comprehensive information on how the measurements were acquired and processed, you can explore the <a href="http://graphics.stanford.edu/data/3Dscanrep/">Stanford Bunny Model</a>.



## Point-to-Plane ICP

The Point-to-Plane Iterative Closest Point (ICP) algorithm aims to find an optimal transformation (rotation $R$ and translation $t$) that aligns two 3D point clouds, $P={p_i}$ and $Q={q_i}$. The objective is to minimize the sum of squared distances between corresponding points in the two clouds, with the addition of a threshold to exclude distant points during the ICP algorithm.

Previously, the Point-to-Point metric was used for ICP, but it showed slower convergence, requiring more iterations for a satisfactory solution. To improve this, the *Point-to-Plane* metric was introduced. In this metric, the closest point is still determined, but the error is projected onto the normal direction from the found point, providing a more effective measure for sampled points.

The objective function to minimize in Point-to-Plane ICP is given by:

$$E = \sum_i \left(\mathbf{n_i} \cdot \left(\mathbf{R_\theta} \mathbf{p_i} + \mathbf{t} - \mathbf{q_j}\right)\right)^2 \rightarrow \mathrm{min},$$

where:

$(\mathbf{n_i})$ represents the normal vector of the $i$-th point in the source point cloud.
$(\mathbf{R_\theta})$ is the 2D rotation matrix with angle $(\theta)$.
$(\mathbf{p_i})$ corresponds to the $i$-th point in the source point cloud.
$(\mathbf{t})$ denotes the translation vector.
$(\mathbf{q_j})$ refers to the $j$-th point in the target point cloud.

To efficiently solve the above minimization problem, the <a href="https://github.com/ReillyBova/Point-Cloud-Registration/tree/master">Point-Cloud-Registration</a> repository utilizes the kdTree algorithm, which significantly improves the convergence rate. This approach is also applied in the current implementation.




## Results

ICP is applied successfully, and unaligned measurements in the *before ICP* figure  meshed into a simple correct bunny which can be seen in the *After ICP* figure.

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/baturalpguven/Stanford_Bunny_ICP/assets/77858949/aa91c3cf-4a26-4d56-90f9-526bd6351844" alt="Before" >
      <p>Before ICP</p>
    </td>
    <td align="center">
      <img src="https://github.com/baturalpguven/Stanford_Bunny_ICP/assets/77858949/2a69f220-448b-4bff-b03d-23a137a9df61" alt="After" >
      <p>After ICP</p>
    </td>
  </tr>
</table>


## Running the Code
To apply ICP to <a href="http://graphics.stanford.edu/data/3Dscanrep/"> Stanford Bunny </a> use following commands

```
python3 icp.py ./bunny/bun045.pts ./bunny/bun000.pts
python3 icp.py ./bunny/bun090.pts ./bunny/bun045.pts
python3 icp.py ./bunny/bun315.pts ./bunny/bun000.pts
python3 icp.py ./bunny/bun270.pts ./bunny/bun315.pts
python3 icp.py ./bunny/bun180.pts ./bunny/bun270.pts
python3 icp.py ./bunny/chin.pts ./bunny/bun315.pts
python3 icp.py ./bunny/ear_back.pts ./bunny/bun180.pts
python3 icp.py ./bunny/top2.pts ./bunny/bun180.pts
python3 icp.py ./bunny/top3.pts ./bunny/bun000.pts

```

To generate the bunny image after ICP alignment run following

```
python3 view_pts_3D_matplotlib.py --mode output
```

To generate the bunny image before ICP alignment run following
```
python3 view_pts_3D_matplotlib.py --mode bunny
```


Replace ` view_pts_3D_matplotlib.py`, and ` icp.py` with the name of your script or executable. The `--mode` is an example command-line argument that you can customize based on your specific use case.

Command Line Arguments:

--mode <str> (default: 'output')
    For After ICP: output for Before ICP: bunny


Feel free to modify the example command and arguments to match the specific command line interface of your project.



## Referances

1. <a href="https://github.com/ReillyBova/Point-Cloud-Registration/tree/master"> Point-Cloud-Registration </a>
2. <a href="https://www.youtube.com/watch?v=QWDM4cFdKrE"> Iterative Closest Point (ICP) - 5 Minutes with Cyrill </a>
3. <a href="https://nbviewer.org/github/niosus/notebooks/blob/master/icp.ipynb"> Jupyter/nbviewer/ICP </a>
4. <a href="http://graphics.stanford.edu/data/3Dscanrep/">Stanford Bunny Model</a>







