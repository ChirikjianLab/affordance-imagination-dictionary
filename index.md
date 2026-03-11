---
layout: default
title: Home
---
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
<div style="display: flex; justify-content: center; align-items: stretch; gap: 20px; flex-wrap: wrap; margin: 1rem 0;">
  <figure style="margin: 0;">
    <img src="resources/monkey-tool.png" alt="Monkey tool imagination" style="height: 320px; width: auto; display: block;">
  </figure>
  <figure style="margin: 0;">
    <img src="resources/robot_imagine.png" alt="Robot imagination" style="height: 320px; width: auto; display: block;">
  </figure>
</div>

## Introduction
This website presents the research outcomes of our group to demonstrate progress toward our funded project goal: using physical simulation to detect and reason about the affordances of objects.

Our central concept is affordance imagination — enabling robots to mentally simulate possible interactions with previously unseen objects. By integrating physics-based reasoning, geometric analysis, and learning methods (from demonstrations and large language models), our robots can classify novel objects, predict functional poses, and execute manipulation strategies without relying on massive amounts of training data.

The works presented here illustrate how affordance imagination bridges the gap between theory and practice: from seating a teddy bear on a previously unseen chair, to predicting hanging poses of tools, to capping containers, to leveraging LLMs for task decomposition. Together, these efforts chart a path toward safe, generalizable, and intelligent robot interaction in household and healthcare environments.

## Object Affordance Dictionary

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

  .reasoning-link {
    display: inline-block;
    margin-bottom: 0.3rem;
    font-weight: 600;
  }

  .video-link {
    display: inline-block;
    margin-bottom: 0.3rem;
    font-weight: 600;
  }

  .video-modal-card {
    width: min(980px, 100%);
    max-height: 84vh;
    overflow: hidden;
    border-radius: 1rem;
    background: #f5fbfa;
    box-shadow: 0 24px 80px rgba(0, 0, 0, 0.25);
  }

  .video-modal-body {
    padding: 1rem;
    background: #fcfefe;
  }

  .video-player {
    width: 100%;
    max-height: 68vh;
    border-radius: 0.75rem;
    background: #000000;
  }

  .reasoning-modal-card {
    width: min(960px, 100%);
    max-height: 84vh;
    overflow: hidden;
    border-radius: 1rem;
    background: #f5fbfa;
    box-shadow: 0 24px 80px rgba(0, 0, 0, 0.25);
  }

  .reasoning-modal-body {
    max-height: min(68vh, 720px);
    overflow: auto;
    padding: 1.25rem;
    background: #fcfefe;
  }

  .reasoning-content {
    margin: 0;
    white-space: pre-wrap;
    line-height: 1.6;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.92rem;
  }

  .model-modal {
    position: fixed;
    inset: 0;
    z-index: 999;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    background: rgba(10, 28, 27, 0.7);
  }

  .model-modal.is-open {
    display: flex;
  }

  .model-modal-card {
    width: min(1080px, 100%);
    max-height: 88vh;
    overflow: hidden;
    border-radius: 1rem;
    background: #f5fbfa;
    box-shadow: 0 24px 80px rgba(0, 0, 0, 0.25);
  }

  .model-modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 1rem 1.25rem;
    border-bottom: 1px solid #d7e7e4;
    background: rgba(255, 255, 255, 0.82);
  }

  .model-modal-meta strong,
  .model-modal-meta code,
  .model-modal-meta small {
    display: block;
  }

  .model-modal-meta small {
    color: #58736f;
  }

  .model-modal-close {
    border: 0;
    border-radius: 999px;
    padding: 0.45rem 0.9rem;
    background: #0f5f52;
    color: #ffffff;
    cursor: pointer;
    font: inherit;
  }

  .model-modal-body {
    position: relative;
    height: min(72vh, 760px);
    background:
      radial-gradient(circle at top, #ffffff 0%, #edf5f3 52%, #d7e9e6 100%);
  }

  .model-viewer-canvas {
    width: 100%;
    height: 100%;
    display: block;
  }

  .model-modal-status {
    position: absolute;
    top: 1rem;
    left: 1rem;
    padding: 0.55rem 0.8rem;
    border: 1px solid #d7e7e4;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.92);
    font-size: 0.92rem;
  }

  @media (max-width: 720px) {
    .model-modal {
      padding: 0.75rem;
    }

    .model-modal-header {
      padding: 0.85rem 1rem;
    }

    .model-modal-body {
      height: 60vh;
    }
  }
</style>

<div class="dictionary-note">
  <strong>Current asset mapping.</strong> The repository contains household object meshes under <code>assets/models/</code> in <code>.obj</code> and <code>.glb</code> format, affordance reasoning profiles under <code>assets/profiles/</code>, and demonstration videos under <code>assets/videos/</code>. Click a model path to open the 3D viewer or click <code>analysis.txt</code> to read the corresponding reasoning.
</div>

<div class="dictionary-section">
  <div class="dictionary-table-wrapper">
    <table class="dictionary-table">
      <thead>
        <tr>
          <th style="width: 4rem;">ID</th>
          <th style="width: 10rem;">Object Name</th>
          <th style="width: 15rem;">3D Model</th>
          <th style="width: 18rem;">Primary Affordance</th>
          <th style="width: 14rem;">Affordance Reasoning</th>
          <th style="width: 20rem;">Interaction Pattern</th>
          <th style="width: 16rem;">Video</th>
        </tr>
      </thead>
      <tbody>
      <tr><td>01</td><td>Ashtray</td><td><a class="model-link" href="#" data-model="assets/models/ashtray.glb" data-name="Ashtray"><code>assets/models/ashtray.glb</code></a><br><small>Click to view 3D model</small></td><td>Collect ash and small discarded items</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/ashtray/analysis.txt" data-name="Ashtray"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">grasp-rim</span><span class="interaction-tag">place-on-surface</span><span class="interaction-tag">drop-into</span></td><td><a class="video-link" href="#" data-video="assets/videos/ashtray.mp4" data-name="Ashtray"><code>assets/videos/ashtray.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>02</td><td>Basin</td><td><a class="model-link" href="#" data-model="assets/models/basin.glb" data-name="Basin"><code>assets/models/basin.glb</code></a><br><small>Click to view 3D model</small></td><td>Contain water or loose objects</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/basin/analysis.txt" data-name="Basin"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">grasp-rim</span><span class="interaction-tag">carry</span><span class="interaction-tag">fill/pour</span></td><td><a class="video-link" href="#" data-video="assets/videos/basin.mp4" data-name="Basin"><code>assets/videos/basin.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>03</td><td>Basket</td><td><a class="model-link" href="#" data-model="assets/models/basket.obj" data-name="Basket"><code>assets/models/basket.obj</code></a><br><small>Click to view 3D model</small></td><td>Store and transport household items</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/basket/analysis.txt" data-name="Basket"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">grasp-handle</span><span class="interaction-tag">carry</span><span class="interaction-tag">load/unload</span></td><td><a class="video-link" href="#" data-video="assets/videos/basket.mp4" data-name="Basket"><code>assets/videos/basket.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>04</td><td>Bathtub</td><td><a class="model-link" href="#" data-model="assets/models/bathtub.glb" data-name="Bathtub"><code>assets/models/bathtub.glb</code></a><br><small>Click to view 3D model</small></td><td>Contain a body for washing or soaking</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/bathtub/analysis.txt" data-name="Bathtub"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">approach</span><span class="interaction-tag">step-in</span><span class="interaction-tag">support-body</span></td><td><a class="video-link" href="#" data-video="assets/videos/bathtub.mp4" data-name="Bathtub"><code>assets/videos/bathtub.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>05</td><td>Bed</td><td><a class="model-link" href="#" data-model="assets/models/bed.glb" data-name="Bed"><code>assets/models/bed.glb</code></a><br><small>Click to view 3D model</small></td><td>Support lying, resting, and sleeping</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/bed/analysis.txt" data-name="Bed"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">approach</span><span class="interaction-tag">sit/lie</span><span class="interaction-tag">reposition-bedding</span></td><td><a class="video-link" href="#" data-video="assets/videos/bed.mp4" data-name="Bed"><code>assets/videos/bed.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>06</td><td>Bottle</td><td><a class="model-link" href="#" data-model="assets/models/bottle.glb" data-name="Bottle"><code>assets/models/bottle.glb</code></a><br><small>Click to view 3D model</small></td><td>Store and pour liquid</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/bottle/analysis.txt" data-name="Bottle"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">wrap-grasp</span><span class="interaction-tag">tilt-pour</span><span class="interaction-tag">set-down</span></td><td><a class="video-link" href="#" data-video="assets/videos/bottle.mp4" data-name="Bottle"><code>assets/videos/bottle.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>07</td><td>Bowl</td><td><a class="model-link" href="#" data-model="assets/models/bowl.glb" data-name="Bowl"><code>assets/models/bowl.glb</code></a><br><small>Click to view 3D model</small></td><td>Contain food or small items</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/bowl/analysis.txt" data-name="Bowl"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">grasp-rim</span><span class="interaction-tag">carry</span><span class="interaction-tag">place</span></td><td><a class="video-link" href="#" data-video="assets/videos/bowl.mp4" data-name="Bowl"><code>assets/videos/bowl.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>08</td><td>Box</td><td><a class="model-link" href="#" data-model="assets/models/box.glb" data-name="Box"><code>assets/models/box.glb</code></a><br><small>Click to view 3D model</small></td><td>Enclose, store, and organize contents</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/box/analysis.txt" data-name="Box"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">grasp-side</span><span class="interaction-tag">open/close</span><span class="interaction-tag">pack</span></td><td><a class="video-link" href="#" data-video="assets/videos/box.mp4" data-name="Box"><code>assets/videos/box.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>09</td><td>Chair</td><td><a class="model-link" href="#" data-model="assets/models/chair.glb" data-name="Chair"><code>assets/models/chair.glb</code></a><br><small>Click to view 3D model</small></td><td>Support sitting posture</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/chair/analysis.txt" data-name="Chair"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">grasp-backrest</span><span class="interaction-tag">pull/push</span><span class="interaction-tag">sit-support</span></td><td><a class="video-link" href="#" data-video="assets/videos/chair.mp4" data-name="Chair"><code>assets/videos/chair.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>10</td><td>Cubby</td><td><a class="model-link" href="#" data-model="assets/models/cubby.glb" data-name="Cubby"><code>assets/models/cubby.glb</code></a><br><small>Click to view 3D model</small></td><td>Compartmentalize and store objects</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/cubby/analysis.txt" data-name="Cubby"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">insert</span><span class="interaction-tag">retrieve</span><span class="interaction-tag">organize</span></td><td><a class="video-link" href="#" data-video="assets/videos/cubby.mp4" data-name="Cubby"><code>assets/videos/cubby.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>11</td><td>Cup</td><td><a class="model-link" href="#" data-model="assets/models/cup.glb" data-name="Cup"><code>assets/models/cup.glb</code></a><br><small>Click to view 3D model</small></td><td>Contain and transport a drink</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/cup/analysis.txt" data-name="Cup"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">grasp-side</span><span class="interaction-tag">lift</span><span class="interaction-tag">drink/pour</span></td><td><a class="video-link" href="#" data-video="assets/videos/cup.mp4" data-name="Cup"><code>assets/videos/cup.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>12</td><td>Cupboard</td><td><a class="model-link" href="#" data-model="assets/models/cupboard.glb" data-name="Cupboard"><code>assets/models/cupboard.glb</code></a><br><small>Click to view 3D model</small></td><td>Store protected household items</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/cupboard/analysis.txt" data-name="Cupboard"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">open-door</span><span class="interaction-tag">shelve</span><span class="interaction-tag">close-door</span></td><td><a class="video-link" href="#" data-video="assets/videos/cupboard.mp4" data-name="Cupboard"><code>assets/videos/cupboard.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>13</td><td>Display Stand</td><td><a class="model-link" href="#" data-model="assets/models/display.glb" data-name="Display Stand"><code>assets/models/display.glb</code></a><br><small>Click to view 3D model</small></td><td>Present and support an object visibly</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/display/analysis.txt" data-name="Display Stand"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">place-object</span><span class="interaction-tag">stabilize</span><span class="interaction-tag">reposition</span></td><td><a class="video-link" href="#" data-video="assets/videos/display.mp4" data-name="Display Stand"><code>assets/videos/display.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>14</td><td>Ladle</td><td><a class="model-link" href="#" data-model="assets/models/ladle.glb" data-name="Ladle"><code>assets/models/ladle.glb</code></a><br><small>Click to view 3D model</small></td><td>Scoop and transfer liquid</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/ladle/analysis.txt" data-name="Ladle"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">grasp-handle</span><span class="interaction-tag">dip</span><span class="interaction-tag">pour-out</span></td><td><a class="video-link" href="#" data-video="assets/videos/ladle.mp4" data-name="Ladle"><code>assets/videos/ladle.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>15</td><td>Plate</td><td><a class="model-link" href="#" data-model="assets/models/plate.glb" data-name="Plate"><code>assets/models/plate.glb</code></a><br><small>Click to view 3D model</small></td><td>Support and present food</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/plate/analysis.txt" data-name="Plate"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">pinch-edge</span><span class="interaction-tag">carry-flat</span><span class="interaction-tag">set-down</span></td><td><a class="video-link" href="#" data-video="assets/videos/plate.mp4" data-name="Plate"><code>assets/videos/plate.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>16</td><td>Pot</td><td><a class="model-link" href="#" data-model="assets/models/pot.glb" data-name="Pot"><code>assets/models/pot.glb</code></a><br><small>Click to view 3D model</small></td><td>Contain and heat ingredients</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/pot/analysis.txt" data-name="Pot"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">grasp-handle</span><span class="interaction-tag">lift</span><span class="interaction-tag">pour</span></td><td><a class="video-link" href="#" data-video="assets/videos/pot.mp4" data-name="Pot"><code>assets/videos/pot.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>17</td><td>Riser</td><td><a class="model-link" href="#" data-model="assets/models/riser.glb" data-name="Riser"><code>assets/models/riser.glb</code></a><br><small>Click to view 3D model</small></td><td>Raise an object to a higher level</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/riser/analysis.txt" data-name="Riser"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">place-under</span><span class="interaction-tag">elevate</span><span class="interaction-tag">stabilize</span></td><td><a class="video-link" href="#" data-video="assets/videos/riser.mp4" data-name="Riser"><code>assets/videos/riser.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>18</td><td>Shelf</td><td><a class="model-link" href="#" data-model="assets/models/shelf.glb" data-name="Shelf"><code>assets/models/shelf.glb</code></a><br><small>Click to view 3D model</small></td><td>Support stored objects vertically</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/shelf/analysis.txt" data-name="Shelf"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">place-object</span><span class="interaction-tag">stack</span><span class="interaction-tag">retrieve</span></td><td><a class="video-link" href="#" data-video="assets/videos/shelf.mp4" data-name="Shelf"><code>assets/videos/shelf.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>19</td><td>Shoe Rack</td><td><a class="model-link" href="#" data-model="assets/models/shoe_rack.glb" data-name="Shoe Rack"><code>assets/models/shoe_rack.glb</code></a><br><small>Click to view 3D model</small></td><td>Organize and store footwear</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/shoe_rack/analysis.txt" data-name="Shoe Rack"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">place-pair</span><span class="interaction-tag">align</span><span class="interaction-tag">retrieve</span></td><td><a class="video-link" href="#" data-video="assets/videos/shoe_rack.mp4" data-name="Shoe Rack"><code>assets/videos/shoe_rack.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>20</td><td>Stool</td><td><a class="model-link" href="#" data-model="assets/models/stool.glb" data-name="Stool"><code>assets/models/stool.glb</code></a><br><small>Click to view 3D model</small></td><td>Support sitting or standing reach</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/stool/analysis.txt" data-name="Stool"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">top-grasp</span><span class="interaction-tag">reposition</span><span class="interaction-tag">step/sit</span></td><td><a class="video-link" href="#" data-video="assets/videos/stool.mp4" data-name="Stool"><code>assets/videos/stool.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>21</td><td>Table</td><td><a class="model-link" href="#" data-model="assets/models/table.glb" data-name="Table"><code>assets/models/table.glb</code></a><br><small>Click to view 3D model</small></td><td>Support placement and workspace use</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/table/analysis.txt" data-name="Table"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">place-object</span><span class="interaction-tag">lean-support</span><span class="interaction-tag">push</span></td><td><a class="video-link" href="#" data-video="assets/videos/table.mp4" data-name="Table"><code>assets/videos/table.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>22</td><td>Trash Bin</td><td><a class="model-link" href="#" data-model="assets/models/trashbin.glb" data-name="Trash Bin"><code>assets/models/trashbin.glb</code></a><br><small>Click to view 3D model</small></td><td>Receive and contain waste</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/trashbin/analysis.txt" data-name="Trash Bin"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">drop-into</span><span class="interaction-tag">grasp-rim</span><span class="interaction-tag">relocate</span></td><td><a class="video-link" href="#" data-video="assets/videos/trashbin.mp4" data-name="Trash Bin"><code>assets/videos/trashbin.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>23</td><td>TV Stand</td><td><a class="model-link" href="#" data-model="assets/models/tv_stand.obj" data-name="TV Stand"><code>assets/models/tv_stand.obj</code></a><br><small>Click to view 3D model</small></td><td>Support media devices at viewing height</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/tv_stand/analysis.txt" data-name="TV Stand"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">place-object</span><span class="interaction-tag">organize-cables</span><span class="interaction-tag">reposition</span></td><td><a class="video-link" href="#" data-video="assets/videos/tv_stand.mp4" data-name="TV Stand"><code>assets/videos/tv_stand.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>24</td><td>Vase</td><td><a class="model-link" href="#" data-model="assets/models/vase.obj" data-name="Vase"><code>assets/models/vase.obj</code></a><br><small>Click to view 3D model</small></td><td>Hold flowers or decorative stems</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/vase/analysis.txt" data-name="Vase"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">grasp-body</span><span class="interaction-tag">insert-stems</span><span class="interaction-tag">place-display</span></td><td><a class="video-link" href="#" data-video="assets/videos/vase.mp4" data-name="Vase"><code>assets/videos/vase.mp4</code></a><br><small>Click to open video</small></td></tr>
      <tr><td>25</td><td>Wine Glass</td><td><a class="model-link" href="#" data-model="assets/models/wine_glass.obj" data-name="Wine Glass"><code>assets/models/wine_glass.obj</code></a><br><small>Click to view 3D model</small></td><td>Contain and present a beverage delicately</td><td><a class="reasoning-link" href="#" data-analysis="assets/profiles/wine_glass/analysis.txt" data-name="Wine Glass"><code>analysis.txt</code></a><br><small>Click to read reasoning</small></td><td><span class="interaction-tag">pinch-stem</span><span class="interaction-tag">lift</span><span class="interaction-tag">sip/place</span></td><td><a class="video-link" href="#" data-video="assets/videos/wine_glass.mp4" data-name="Wine Glass"><code>assets/videos/wine_glass.mp4</code></a><br><small>Click to open video</small></td></tr>
      </tbody>
    </table>
  </div>
</div>

<div class="model-modal" id="model-modal" aria-hidden="true">
  <div class="model-modal-card" role="dialog" aria-modal="true" aria-labelledby="model-modal-title">
    <div class="model-modal-header">
      <div class="model-modal-meta">
        <strong id="model-modal-title">3D Model Viewer</strong>
        <code id="model-modal-path">assets/example</code>
        <small>Drag to rotate. Scroll to zoom. Right-drag to pan.</small>
      </div>
      <button class="model-modal-close" id="model-modal-close" type="button">Close</button>
    </div>
    <div class="model-modal-body">
      <div class="model-modal-status" id="model-modal-status">Loading viewer...</div>
      <canvas class="model-viewer-canvas" id="model-viewer-canvas"></canvas>
    </div>
  </div>
</div>

<div class="model-modal" id="reasoning-modal" aria-hidden="true">
  <div class="reasoning-modal-card" role="dialog" aria-modal="true" aria-labelledby="reasoning-modal-title">
    <div class="model-modal-header">
      <div class="model-modal-meta">
        <strong id="reasoning-modal-title">Affordance Reasoning</strong>
        <code id="reasoning-modal-path">assets/profiles/example/analysis.txt</code>
        <small>Click outside the window or press Escape to close.</small>
      </div>
      <button class="model-modal-close" id="reasoning-modal-close" type="button">Close</button>
    </div>
    <div class="reasoning-modal-body">
      <pre class="reasoning-content" id="reasoning-content">Loading analysis...</pre>
    </div>
  </div>
</div>

<div class="model-modal" id="video-modal" aria-hidden="true">
  <div class="video-modal-card" role="dialog" aria-modal="true" aria-labelledby="video-modal-title">
    <div class="model-modal-header">
      <div class="model-modal-meta">
        <strong id="video-modal-title">Object Video</strong>
        <code id="video-modal-path">assets/videos/example.mp4</code>
        <small>Play the video in the current page.</small>
      </div>
      <button class="model-modal-close" id="video-modal-close" type="button">Close</button>
    </div>
    <div class="video-modal-body">
      <video class="video-player" id="video-player" controls preload="metadata"></video>
    </div>
  </div>
</div>

<script type="importmap">
{
  "imports": {
    "three": "https://esm.sh/three@0.160.0",
    "three/examples/jsm/controls/OrbitControls": "https://esm.sh/three@0.160.0/examples/jsm/controls/OrbitControls",
    "three/examples/jsm/loaders/OBJLoader": "https://esm.sh/three@0.160.0/examples/jsm/loaders/OBJLoader",
    "three/examples/jsm/loaders/GLTFLoader": "https://esm.sh/three@0.160.0/examples/jsm/loaders/GLTFLoader"
  }
}
</script>

<script type="module">
  import * as THREE from "three";
  import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
  import { OBJLoader } from "three/examples/jsm/loaders/OBJLoader";
  import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";

  const modal = document.getElementById("model-modal");
  const closeButton = document.getElementById("model-modal-close");
  const titleElement = document.getElementById("model-modal-title");
  const pathElement = document.getElementById("model-modal-path");
  const statusElement = document.getElementById("model-modal-status");
  const canvas = document.getElementById("model-viewer-canvas");
  const modelLinks = document.querySelectorAll(".model-link");
  const reasoningModal = document.getElementById("reasoning-modal");
  const reasoningCloseButton = document.getElementById("reasoning-modal-close");
  const reasoningTitleElement = document.getElementById("reasoning-modal-title");
  const reasoningPathElement = document.getElementById("reasoning-modal-path");
  const reasoningContentElement = document.getElementById("reasoning-content");
  const reasoningLinks = document.querySelectorAll(".reasoning-link");
  const videoModal = document.getElementById("video-modal");
  const videoCloseButton = document.getElementById("video-modal-close");
  const videoTitleElement = document.getElementById("video-modal-title");
  const videoPathElement = document.getElementById("video-modal-path");
  const videoPlayer = document.getElementById("video-player");
  const videoLinks = document.querySelectorAll(".video-link");

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xedf5f3);

  const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 1000);
  const controls = new OrbitControls(camera, canvas);
  const objLoader = new OBJLoader();
  const gltfLoader = new GLTFLoader();

  let currentObject = null;

  controls.enableDamping = true;
  controls.dampingFactor = 0.08;

  scene.add(new THREE.HemisphereLight(0xffffff, 0xc2ddd8, 1.5));
  const dirLight = new THREE.DirectionalLight(0xffffff, 1.15);
  dirLight.position.set(4, 5, 4);
  scene.add(dirLight);

  const ground = new THREE.Mesh(
    new THREE.CircleGeometry(2.6, 64),
    new THREE.MeshBasicMaterial({ color: 0xdbeae7 })
  );
  ground.rotation.x = -Math.PI / 2;
  ground.position.y = -1.25;
  scene.add(ground);

  function resizeRenderer() {
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    if (!width || !height) {
      return;
    }
    renderer.setSize(width, height, false);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
  }

  function animate() {
    resizeRenderer();
    controls.update();
    renderer.render(scene, camera);
    requestAnimationFrame(animate);
  }

  function clearCurrentObject() {
    if (!currentObject) {
      return;
    }
    scene.remove(currentObject);
    currentObject.traverse((child) => {
      if (child.isMesh && child.material) {
        child.material.dispose();
      }
    });
    currentObject = null;
  }

  function fitCameraToObject(object) {
    const box = new THREE.Box3().setFromObject(object);
    const size = box.getSize(new THREE.Vector3());
    const center = box.getCenter(new THREE.Vector3());
    const maxDim = Math.max(size.x, size.y, size.z) || 1;
    const fitHeightDistance = maxDim / (2 * Math.tan((Math.PI * camera.fov) / 360));
    const fitWidthDistance = fitHeightDistance / camera.aspect;
    const distance = 1.25 * Math.max(fitHeightDistance, fitWidthDistance);

    controls.target.copy(center);
    camera.position.set(center.x + distance * 0.65, center.y + distance * 0.45, center.z + distance);
    camera.near = Math.max(distance / 100, 0.01);
    camera.far = distance * 100;
    camera.updateProjectionMatrix();
    controls.update();

    ground.position.set(center.x, box.min.y - maxDim * 0.22, center.z);
    ground.scale.setScalar(Math.max(maxDim, 1));
  }

  function applyDefaultMaterials(object) {
    object.traverse((child) => {
      if (!child.isMesh) {
        return;
      }
      if (!child.material) {
        child.material = new THREE.MeshStandardMaterial({
          color: 0x7aa8a1,
          roughness: 0.78,
          metalness: 0.08
        });
      }
      child.castShadow = false;
      child.receiveShadow = false;
    });
  }

  function loadModel(modelPath) {
    const extension = modelPath.split(".").pop().toLowerCase();

    if (extension === "glb" || extension === "gltf") {
      return new Promise((resolve, reject) => {
        gltfLoader.load(
          modelPath,
          (gltf) => resolve(gltf.scene),
          undefined,
          reject
        );
      });
    }

    return new Promise((resolve, reject) => {
      objLoader.load(
        modelPath,
        resolve,
        undefined,
        reject
      );
    });
  }

  function openModal(modelPath, modelName) {
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    titleElement.textContent = modelName;
    pathElement.textContent = modelPath;
    statusElement.textContent = "Loading model...";
    resizeRenderer();
    clearCurrentObject();

    loadModel(modelPath).then((object) => {
        applyDefaultMaterials(object);
        currentObject = object;
        scene.add(object);
        fitCameraToObject(object);
        statusElement.textContent = "Model loaded";
      }).catch(() => {
        statusElement.textContent = "Failed to load model";
      });
  }

  function closeModal() {
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    clearCurrentObject();
    statusElement.textContent = "Loading viewer...";
  }

  function openReasoningModal(analysisPath, objectName) {
    reasoningModal.classList.add("is-open");
    reasoningModal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    reasoningTitleElement.textContent = objectName + " Affordance Reasoning";
    reasoningPathElement.textContent = analysisPath;
    reasoningContentElement.textContent = "Loading analysis...";

    fetch(analysisPath)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to load analysis");
        }
        return response.text();
      })
      .then((text) => {
        reasoningContentElement.textContent = text;
      })
      .catch(() => {
        reasoningContentElement.textContent = "Failed to load analysis.";
      });
  }

  function closeReasoningModal() {
    reasoningModal.classList.remove("is-open");
    reasoningModal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    reasoningContentElement.textContent = "Loading analysis...";
  }

  function openVideoModal(videoPath, objectName) {
    videoModal.classList.add("is-open");
    videoModal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    videoTitleElement.textContent = objectName + " Video";
    videoPathElement.textContent = videoPath;
    videoPlayer.src = videoPath;
    videoPlayer.load();
  }

  function closeVideoModal() {
    videoModal.classList.remove("is-open");
    videoModal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    videoPlayer.pause();
    videoPlayer.removeAttribute("src");
    videoPlayer.load();
  }

  modelLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      openModal(link.dataset.model, link.dataset.name);
    });
  });

  reasoningLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      openReasoningModal(link.dataset.analysis, link.dataset.name);
    });
  });

  videoLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      openVideoModal(link.dataset.video, link.dataset.name);
    });
  });

  closeButton.addEventListener("click", closeModal);
  modal.addEventListener("click", (event) => {
    if (event.target === modal) {
      closeModal();
    }
  });
  reasoningCloseButton.addEventListener("click", closeReasoningModal);
  reasoningModal.addEventListener("click", (event) => {
    if (event.target === reasoningModal) {
      closeReasoningModal();
    }
  });
  videoCloseButton.addEventListener("click", closeVideoModal);
  videoModal.addEventListener("click", (event) => {
    if (event.target === videoModal) {
      closeVideoModal();
    }
  });
  window.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      if (modal.classList.contains("is-open")) {
        closeModal();
      }
      if (reasoningModal.classList.contains("is-open")) {
        closeReasoningModal();
      }
      if (videoModal.classList.contains("is-open")) {
        closeVideoModal();
      }
    }
  });

  animate();
</script>

This table now reflects the actual contents of your `assets` folder. Click any model link to open a centered in-page viewer. When you add videos, replace each placeholder path with a local file, a linked thumbnail, or an embedded player.

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
