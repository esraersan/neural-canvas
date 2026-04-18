# NeuralCanvas 🧠🎨

> Bridging human perception and generative AI.

EEG-to-image reconstruction pipeline benchmarking how well AI vision models align with human neural representations — and how fast.

Uses THINGS-EEG2 and ECOSET to compare EEG encoder architectures (EEGNet, BENDR, ATM, ViT-EEG) against CLIP, DINO, and ViT via Representational Similarity Analysis, then reconstructs perceived images by conditioning Stable Diffusion XL on EEG-derived CLIP latents.

![Architecture](assets/neuralcanvas2.png)

---

**Stack:** PyTorch · Triton · OpenCLIP · Stable Diffusion XL · MNE · Nsight Systems

🚧 Active development
