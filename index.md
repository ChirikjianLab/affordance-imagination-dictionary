[Xiaoli Wang<sup>1</sup>](https://github.com/lily983){:target="_blank"}, [Sipu Ruan<sup>1</sup>](https://ruansp.github.io/){:target="_blank"}, [Xin Meng<sup>1</sup>](https://github.com/XinnMeng){:target="_blank"}, 
[Hongtao Wu<sup>1</sup>](https://github.com/ChirikjianLab){:target="_blank"},
[Wanze Li<sup>1</sup>](https://github.com/ChirikjianLab){:target="_blank"},
[Zhanhong Sun<sup>1</sup>](https://github.com/ChirikjianLab){:target="_blank"},
[Yuwei Wu<sup>1</sup>](https://github.com/ChirikjianLab){:target="_blank"},
[Ceng Zhang<sup>1</sup>](https://github.com/ChirikjianLab){:target="_blank"},
[Wan Su<sup>1</sup>](https://github.com/ChirikjianLab){:target="_blank"}, 
[Chen Dong<sup>2</sup>](https://github.com/ChirikjianLab){:target="_blank"}, 
[Cecilia Laschi<sup>12*</sup>](https://scholar.google.com/citations?user=1vR7lMUAAAAJ&hl=en){:target="_blank"}
[Gregory Chirikjian<sup>12*</sup>](https://cde.nus.edu.sg/me/staff/chirikjian-gregory-s/){:target="_blank"}

<sup>1</sup>Department of Mechanical Engineering, National University of Singapore, Singapore

<sup>2</sup>Department of Mechanical Engineering, University of Delaware, USA

<sup>*</sup>Principal Investigator


## Motivation: Learning Affordances Through Play
Just like this monkey experimenting with stones, humans learn to use tools by playing, testing, and discovering their affordances. A stick can become a lever, a rock can become a hammer — but this is not taught directly. Instead, it emerges through interaction and imagination.

This project takes inspiration from this natural process. Our goal is to enable robots to:

- Imagine possible uses of unfamiliar objects, much like humans and animals.

- Simulate physical interactions in a virtual environment before acting in the real world.

- Discover affordances — the actionable possibilities an object provides — without needing massive labeled datasets.

This biological analogy underpins our concept of Affordance Imagination: giving robots the ability to reason about function through simulation and exploration, the same way evolution equipped primates and humans with the ability to learn tools by trying them out.
<figure style="text-align: center;">
  <img src="resources/monkey-tool.png" alt="Motivation" width="500">
</figure>

## Introduction
This website presents the research outcomes of our group to demonstrate progress toward our funded project goal: using physical simulation to detect and reason about the affordances of objects.

Our central concept is affordance imagination — enabling robots to mentally simulate possible interactions with previously unseen objects. By integrating physics-based reasoning, geometric analysis, and learning methods (from demonstrations and large language models), our robots can classify novel objects, predict functional poses, and execute manipulation strategies without relying on massive amounts of training data.

The works presented here illustrate how affordance imagination bridges the gap between theory and practice: from seating a teddy bear on a previously unseen chair, to predicting hanging poses of tools, to capping containers, to leveraging LLMs for task decomposition. Together, these efforts chart a path toward safe, generalizable, and intelligent robot interaction in household and healthcare environments.

## Affordance Dictionary

This section is designed as a compact catalog for common household objects that can support affordance reasoning, simulation, and demonstration. Each entry records the object category, the 3D asset link, the main affordance, the dominant interaction pattern, and the corresponding demonstration video.

<style>
  .dictionary-note {
    margin-bottom: 1rem;
    padding: 0.9rem 1rem;
    border-left: 4px solid #157878;
    background: #f4fbfa;
  }

  .dictionary-table-wrapper {
    overflow-x: auto;
    margin: 1.25rem 0 2rem 0;
  }

  .dictionary-table {
    width: 100%;
    min-width: 980px;
    border-collapse: collapse;
    font-size: 0.96rem;
  }

  .dictionary-table th,
  .dictionary-table td {
    padding: 0.8rem 0.9rem;
    border: 1px solid #d7e7e4;
    vertical-align: top;
  }

  .dictionary-table th {
    background: #e7f4f1;
    color: #0f3d39;
    text-align: left;
    white-space: nowrap;
  }

  .dictionary-table tr:nth-child(even) {
    background: #fbfdfd;
  }

  .interaction-tag {
    display: inline-block;
    padding: 0.2rem 0.45rem;
    margin: 0.1rem 0.2rem 0.1rem 0;
    border-radius: 0.35rem;
    background: #f3efe4;
    color: #5f4a12;
    font-size: 0.84rem;
  }

  .model-link {
    display: inline-block;
    margin-bottom: 0.3rem;
    font-weight: 600;
  }

  .video-placeholder {
    display: inline-block;
    padding: 0.2rem 0.5rem;
    border-radius: 999px;
    background: #fff3d9;
    color: #8c5b13;
    font-size: 0.82rem;
    font-weight: 600;
  }
</style>

<div class="dictionary-note">
  <strong>Current asset mapping.</strong> The repository already contains 25 object meshes under <code>assets/</code> in <code>.obj</code> format. The table links each asset to a separate viewer page so the main page stays lightweight. Video files are not present yet, so the last column keeps a ready-to-fill placeholder path for each object.
</div>

<div class="dictionary-table-wrapper">
  <table class="dictionary-table">
    <thead>
      <tr>
        <th style="width: 4rem;">ID</th>
        <th style="width: 10rem;">Object Name</th>
        <th style="width: 15rem;">3D Model</th>
        <th style="width: 18rem;">Primary Affordance</th>
        <th style="width: 20rem;">Interaction Pattern</th>
        <th style="width: 15rem;">Video</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>01</td><td>Ashtray</td><td><a class="model-link" href="viewer.html?model=assets/ashtray.obj&name=Ashtray" target="_blank"><code>assets/ashtray.obj</code></a><br><small>Click to view 3D model</small></td><td>Collect ash and small discarded items</td><td><span class="interaction-tag">grasp-rim</span><span class="interaction-tag">place-on-surface</span><span class="interaction-tag">drop-into</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/ashtray.mp4</code></td></tr>
      <tr><td>02</td><td>Basin</td><td><a class="model-link" href="viewer.html?model=assets/basin.obj&name=Basin" target="_blank"><code>assets/basin.obj</code></a><br><small>Click to view 3D model</small></td><td>Contain water or loose objects</td><td><span class="interaction-tag">grasp-rim</span><span class="interaction-tag">carry</span><span class="interaction-tag">fill/pour</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/basin.mp4</code></td></tr>
      <tr><td>03</td><td>Basket</td><td><a class="model-link" href="viewer.html?model=assets/basket.obj&name=Basket" target="_blank"><code>assets/basket.obj</code></a><br><small>Click to view 3D model</small></td><td>Store and transport household items</td><td><span class="interaction-tag">grasp-handle</span><span class="interaction-tag">carry</span><span class="interaction-tag">load/unload</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/basket.mp4</code></td></tr>
      <tr><td>04</td><td>Bathtub</td><td><a class="model-link" href="viewer.html?model=assets/bathtub.obj&name=Bathtub" target="_blank"><code>assets/bathtub.obj</code></a><br><small>Click to view 3D model</small></td><td>Contain a body for washing or soaking</td><td><span class="interaction-tag">approach</span><span class="interaction-tag">step-in</span><span class="interaction-tag">support-body</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/bathtub.mp4</code></td></tr>
      <tr><td>05</td><td>Bed</td><td><a class="model-link" href="viewer.html?model=assets/bed.obj&name=Bed" target="_blank"><code>assets/bed.obj</code></a><br><small>Click to view 3D model</small></td><td>Support lying, resting, and sleeping</td><td><span class="interaction-tag">approach</span><span class="interaction-tag">sit/lie</span><span class="interaction-tag">reposition-bedding</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/bed.mp4</code></td></tr>
      <tr><td>06</td><td>Bottle</td><td><a class="model-link" href="viewer.html?model=assets/bottle.obj&name=Bottle" target="_blank"><code>assets/bottle.obj</code></a><br><small>Click to view 3D model</small></td><td>Store and pour liquid</td><td><span class="interaction-tag">wrap-grasp</span><span class="interaction-tag">tilt-pour</span><span class="interaction-tag">set-down</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/bottle.mp4</code></td></tr>
      <tr><td>07</td><td>Bowl</td><td><a class="model-link" href="viewer.html?model=assets/bowl.obj&name=Bowl" target="_blank"><code>assets/bowl.obj</code></a><br><small>Click to view 3D model</small></td><td>Contain food or small items</td><td><span class="interaction-tag">grasp-rim</span><span class="interaction-tag">carry</span><span class="interaction-tag">place</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/bowl.mp4</code></td></tr>
      <tr><td>08</td><td>Box</td><td><a class="model-link" href="viewer.html?model=assets/box.obj&name=Box" target="_blank"><code>assets/box.obj</code></a><br><small>Click to view 3D model</small></td><td>Enclose, store, and organize contents</td><td><span class="interaction-tag">grasp-side</span><span class="interaction-tag">open/close</span><span class="interaction-tag">pack</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/box.mp4</code></td></tr>
      <tr><td>09</td><td>Chair</td><td><a class="model-link" href="viewer.html?model=assets/chair.obj&name=Chair" target="_blank"><code>assets/chair.obj</code></a><br><small>Click to view 3D model</small></td><td>Support sitting posture</td><td><span class="interaction-tag">grasp-backrest</span><span class="interaction-tag">pull/push</span><span class="interaction-tag">sit-support</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/chair.mp4</code></td></tr>
      <tr><td>10</td><td>Cubby</td><td><a class="model-link" href="viewer.html?model=assets/cubby.obj&name=Cubby" target="_blank"><code>assets/cubby.obj</code></a><br><small>Click to view 3D model</small></td><td>Compartmentalize and store objects</td><td><span class="interaction-tag">insert</span><span class="interaction-tag">retrieve</span><span class="interaction-tag">organize</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/cubby.mp4</code></td></tr>
      <tr><td>11</td><td>Cup</td><td><a class="model-link" href="viewer.html?model=assets/cup.obj&name=Cup" target="_blank"><code>assets/cup.obj</code></a><br><small>Click to view 3D model</small></td><td>Contain and transport a drink</td><td><span class="interaction-tag">grasp-side</span><span class="interaction-tag">lift</span><span class="interaction-tag">drink/pour</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/cup.mp4</code></td></tr>
      <tr><td>12</td><td>Cupboard</td><td><a class="model-link" href="viewer.html?model=assets/cupboard.obj&name=Cupboard" target="_blank"><code>assets/cupboard.obj</code></a><br><small>Click to view 3D model</small></td><td>Store protected household items</td><td><span class="interaction-tag">open-door</span><span class="interaction-tag">shelve</span><span class="interaction-tag">close-door</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/cupboard.mp4</code></td></tr>
      <tr><td>13</td><td>Display Stand</td><td><a class="model-link" href="viewer.html?model=assets/display.obj&name=Display%20Stand" target="_blank"><code>assets/display.obj</code></a><br><small>Click to view 3D model</small></td><td>Present and support an object visibly</td><td><span class="interaction-tag">place-object</span><span class="interaction-tag">stabilize</span><span class="interaction-tag">reposition</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/display.mp4</code></td></tr>
      <tr><td>14</td><td>Ladle</td><td><a class="model-link" href="viewer.html?model=assets/ladle.obj&name=Ladle" target="_blank"><code>assets/ladle.obj</code></a><br><small>Click to view 3D model</small></td><td>Scoop and transfer liquid</td><td><span class="interaction-tag">grasp-handle</span><span class="interaction-tag">dip</span><span class="interaction-tag">pour-out</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/ladle.mp4</code></td></tr>
      <tr><td>15</td><td>Plate</td><td><a class="model-link" href="viewer.html?model=assets/plate.obj&name=Plate" target="_blank"><code>assets/plate.obj</code></a><br><small>Click to view 3D model</small></td><td>Support and present food</td><td><span class="interaction-tag">pinch-edge</span><span class="interaction-tag">carry-flat</span><span class="interaction-tag">set-down</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/plate.mp4</code></td></tr>
      <tr><td>16</td><td>Pot</td><td><a class="model-link" href="viewer.html?model=assets/pot.obj&name=Pot" target="_blank"><code>assets/pot.obj</code></a><br><small>Click to view 3D model</small></td><td>Contain and heat ingredients</td><td><span class="interaction-tag">grasp-handle</span><span class="interaction-tag">lift</span><span class="interaction-tag">pour</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/pot.mp4</code></td></tr>
      <tr><td>17</td><td>Riser</td><td><a class="model-link" href="viewer.html?model=assets/riser.obj&name=Riser" target="_blank"><code>assets/riser.obj</code></a><br><small>Click to view 3D model</small></td><td>Raise an object to a higher level</td><td><span class="interaction-tag">place-under</span><span class="interaction-tag">elevate</span><span class="interaction-tag">stabilize</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/riser.mp4</code></td></tr>
      <tr><td>18</td><td>Shelf</td><td><a class="model-link" href="viewer.html?model=assets/shelf.obj&name=Shelf" target="_blank"><code>assets/shelf.obj</code></a><br><small>Click to view 3D model</small></td><td>Support stored objects vertically</td><td><span class="interaction-tag">place-object</span><span class="interaction-tag">stack</span><span class="interaction-tag">retrieve</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/shelf.mp4</code></td></tr>
      <tr><td>19</td><td>Shoe Rack</td><td><a class="model-link" href="viewer.html?model=assets/shoe_rack.obj&name=Shoe%20Rack" target="_blank"><code>assets/shoe_rack.obj</code></a><br><small>Click to view 3D model</small></td><td>Organize and store footwear</td><td><span class="interaction-tag">place-pair</span><span class="interaction-tag">align</span><span class="interaction-tag">retrieve</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/shoe_rack.mp4</code></td></tr>
      <tr><td>20</td><td>Stool</td><td><a class="model-link" href="viewer.html?model=assets/stool.obj&name=Stool" target="_blank"><code>assets/stool.obj</code></a><br><small>Click to view 3D model</small></td><td>Support sitting or standing reach</td><td><span class="interaction-tag">top-grasp</span><span class="interaction-tag">reposition</span><span class="interaction-tag">step/sit</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/stool.mp4</code></td></tr>
      <tr><td>21</td><td>Table</td><td><a class="model-link" href="viewer.html?model=assets/table.obj&name=Table" target="_blank"><code>assets/table.obj</code></a><br><small>Click to view 3D model</small></td><td>Support placement and workspace use</td><td><span class="interaction-tag">place-object</span><span class="interaction-tag">lean-support</span><span class="interaction-tag">push</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/table.mp4</code></td></tr>
      <tr><td>22</td><td>Trash Bin</td><td><a class="model-link" href="viewer.html?model=assets/trashbin.obj&name=Trash%20Bin" target="_blank"><code>assets/trashbin.obj</code></a><br><small>Click to view 3D model</small></td><td>Receive and contain waste</td><td><span class="interaction-tag">drop-into</span><span class="interaction-tag">grasp-rim</span><span class="interaction-tag">relocate</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/trashbin.mp4</code></td></tr>
      <tr><td>23</td><td>TV Stand</td><td><a class="model-link" href="viewer.html?model=assets/tv_stand.obj&name=TV%20Stand" target="_blank"><code>assets/tv_stand.obj</code></a><br><small>Click to view 3D model</small></td><td>Support media devices at viewing height</td><td><span class="interaction-tag">place-object</span><span class="interaction-tag">organize-cables</span><span class="interaction-tag">reposition</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/tv_stand.mp4</code></td></tr>
      <tr><td>24</td><td>Vase</td><td><a class="model-link" href="viewer.html?model=assets/vase.obj&name=Vase" target="_blank"><code>assets/vase.obj</code></a><br><small>Click to view 3D model</small></td><td>Hold flowers or decorative stems</td><td><span class="interaction-tag">grasp-body</span><span class="interaction-tag">insert-stems</span><span class="interaction-tag">place-display</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/vase.mp4</code></td></tr>
      <tr><td>25</td><td>Wine Glass</td><td><a class="model-link" href="viewer.html?model=assets/wine_glass.obj&name=Wine%20Glass" target="_blank"><code>assets/wine_glass.obj</code></a><br><small>Click to view 3D model</small></td><td>Contain and present a beverage delicately</td><td><span class="interaction-tag">pinch-stem</span><span class="interaction-tag">lift</span><span class="interaction-tag">sip/place</span></td><td><span class="video-placeholder">Video needed</span><br><code>assets/videos/wine_glass.mp4</code></td></tr>
    </tbody>
  </table>
</div>

This table now reflects the actual contents of your `assets` folder. Click any model link to open a dedicated viewer page. When you add videos, replace each placeholder path with a local file, a linked thumbnail, or an embedded player.

## Related Works

### Put a Lid on It! A Learning-Free Method to Cap a Container via Physical Simulations (UR 2025)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/lid.png" alt="lid" width="300"> </figure> <p style="max-width: 500px;"> Develops a simulation-based method for matching unseen containers and lids. Uses Gaussian process distance fields and matching imagination to achieve over 91% success rate. <a href="https://github.com/ChirikjianLab" target="_blank">Code</a>. </p> </div>

### Goal-Guided Reinforcement Learning: Leveraging Large Language Models for Long-Horizon Task Decomposition (ICRA 2025)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/g2rl.png" alt="g2rl" width="300"> </figure> <p style="max-width: 500px;"> Proposes G2RL, where LLMs generate subgoals to help reinforcement learning explore efficiently in long-horizon tasks. Validated across simulated environments with improved convergence. <a href="https://github.com/ChirikjianLab" target="_blank">Code</a>. </p> </div>


### RAIL: Robot Affordance Imagination with Large Language Models (ISER 2025)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/rail.png" alt="rail" width="300"> </figure> <p style="max-width: 500px;"> Combines LLMs with physics-based simulation for automatic affordance reasoning. From minimal semantic input, robots classify novel objects, predict functional poses, and perform unseen tasks. <a href="https://github.com/ChirikjianLab" target="_blank">Code</a>. </p> </div>

### RaggeDi: Diffusion-based State Estimation of Disordered Rags, Sheets, Towels and Blankets (arXiv 2024)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/raggedi.png" alt="raggedi" width="300"> </figure> <p style="max-width: 500px;"> Applies diffusion models for cloth state estimation. Represents cloth deformation as a translation map and achieves superior accuracy in both simulation and real-world experiments. <a href="https://github.com/ChirikjianLab" target="_blank">Code</a>. </p> </div>

### PRIMP: PRobabilistically-Informed Motion Primitives for Efficient Affordance Learning from Demonstration (T-RO 2024)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/primp.png" alt="primp" width="300"> </figure> <p style="max-width: 500px;"> Introduces PRIMP, which learns probabilistic motion primitives from demonstrations and integrates them with workspace-aware motion planning (Workspace-STOMP). Demonstrated on tool-use and affordance-based tasks. <a href="https://github.com/ChirikjianLab" target="_blank">Code</a>. </p> </div>

### Grasping by Hanging: A Learning-Free Grasping Detection Method for Previously Unseen Objects (arXiv 2024)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/grasping-hanging.png" alt="grasping-hanging" width="300"> </figure> <p style="max-width: 500px;"> Introduces Grasping-by-Hanging (GbH), a learning-free approach where robots detect hangable structures to derive grasping poses. Particularly effective for thin or flat objects. <a href="https://github.com/ChirikjianLab" target="_blank">Code</a>. </p> </div>

### I Get the Hang of It! A Learning-Free Method to Predict Hanging Poses for Previously Unseen Objects (RA-L 2024)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/hanging.png" alt="hanging" width="300"> </figure> <p style="max-width: 500px;"> Proposes a learning-free framework for predicting stable hanging poses using geometric and mechanical analysis. Outperforms learning-based baselines in simulation and real-world tests. <a href="https://github.com/ChirikjianLab" target="_blank">Code</a>. </p> </div>


### Prepare the Chair for the Bear! Robot Imagination of Sitting Affordance to Reorient Previously Unseen Chairs (RA-L 2023)
<div style="display: flex; align-items: center;">
  <figure style="margin: 0; margin-right: 20px;">
    <img src="resources/prepare-chair.png" alt="prepare-chair" width="300">
  </figure>
  <p style="max-width: 500px;">
    Robots reconstruct previously unseen chairs, simulate their sitting affordance, 
    and reorient them so a humanoid agent (teddy bear proxy) can be seated. 
    Demonstrates object classification and functional pose prediction via 
    physics-based imagination. <a href="https://github.com/ChirikjianLab" target="_blank">Code</a>.
  </p>
</div>

### Put the Bear on the Chair! Intelligent Robot Interaction with Previously Unseen Chairs via Robot Imagination (arXiv 2022)
<div style="display: flex; align-items: center;"> <figure style="margin: 0; margin-right: 20px;"> <img src="resources/bear-chair.png" alt="bear-chair" width="300"> </figure> <p style="max-width: 500px;"> Extends chair affordance reasoning by enabling a humanoid robot to physically seat a teddy bear. Introduces a human-assistance module to adjust inaccessible chair poses via natural language instructions. <a href="https://github.com/ChirikjianLab" target="_blank">Code</a>. </p> </div>
