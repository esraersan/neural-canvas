cortexbench 🧠
How fast can we decode what the brain sees?
End-to-end benchmark of EEG-to-image reconstruction pipelines — from raw brain signals to reconstructed images. Built around THINGS-EEG2, custom Triton preprocessing kernels, and a systematic sweep of encoder architectures, CLIP alignment, and diffusion decoding across FP32/FP16/INT8.
The goal is a latency-quality frontier: given a real-time constraint, which pipeline wins?

Stack: PyTorch · Triton · TensorRT · OpenCLIP · Stable Diffusion XL · Nsight Systems

