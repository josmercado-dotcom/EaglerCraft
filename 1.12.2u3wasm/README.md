# MCJS 1.12.2 u3 WASM (WASM 版) — 本地镜像

技术：TeaVM → WebAssembly（WASM-GC），WebGL 渲染。

## 文件
- `index.html` — 入口（用户协议弹窗 + eaglercraftXOpts）
- `bootstrap.js` — 加载器（校验 EPW 并提取内嵌 loader.js / loader.wasm）
- `assets.epw` — 加密资源包（EAG$WASM 魔数校验通过）

## 启动
```bash
cd "C:/Users/Administrator/Desktop/MCJS/1.12.2u3wasm"
python -m http.server 8080   # 或直接访问统一服务 http://localhost:8080/1.12.2u3wasm/
```

Eaglercraft 1.12.2 WASM-GC u3，新增导出世界和远程联机支持。
