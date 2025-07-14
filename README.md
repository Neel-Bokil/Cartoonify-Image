# 🎨 Cartoonify Images with Streamlit

> **Turn your photos into stunning cartoons using Computer Vision — all in a Streamlit web app!**


---

## ✨ Project Overview

This project uses OpenCV to transform images into cartoon-like artworks. It’s wrapped in an interactive **Streamlit web app** where users can:

✅ Upload their own photos  
✅ See cartoonified results instantly  
✅ Download the cartoon images

It’s a fun, practical application of image processing and a great way to explore computer vision pipelines.

---

## 🖼️ How Cartoonification Works

The cartoonification process includes:

- **Grayscale Conversion** → simplifies the image  
- **Median Blur** → reduces noise  
- **Adaptive Thresholding** → detects strong edges  
- **Bilateral Filtering** → smooths colors while preserving edges  
- **Masking** → combines edges with the smoothed image for a cartoon effect

---

## 🚀 Try It Locally

Clone this repository:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
