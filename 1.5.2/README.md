# MCJS 1.5.2 (JS 版) — 本地镜像

技术：TeaVM 将 Minecraft Java 字节码编译为 JavaScript，WebGL 渲染。

## 文件
- `index.html` — 入口（用户协议弹窗 + eaglercraftXOpts）
- `classes.js` — 游戏主体（TeaVM 编译 JS）
- `assets.epk` — 加密资源包（EAGP 魔数校验通过）
- `eagswebrtc.js` — WebRTC 联机支持

## 启动
```bash
cd "C:/Users/Administrator/Desktop/MCJS/1.5.2"
python -m http.server 8080
```
