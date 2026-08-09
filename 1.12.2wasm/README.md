# MCJS 1.12.2 WASM 版 — 本地镜像

镜像源：`play.mcjs.144449.xyz/1.12.2wasm/`

技术：TeaVM → WebAssembly（WASM-GC），WebGL 渲染。通过 `bootstrap.js` 加载 `assets.epw`（Eaglercraft WASM 加密格式）。

## 文件清单

| 文件 | 大小 | 作用 |
|------|------|------|
| `index.html` | 3.0 KB | 入口：许可协议弹窗 + eaglercraftXOpts |
| `bootstrap.js` | 7.8 KB | 加载器（含 base64 解码器，校验 EPW 并提取内嵌组件）|
| `assets.epw` | 15.9 MB | 加密资源包（EAG$WASM magic 校验通过），内含 splash.png、loader.js、loader.wasm 及游戏数据 |
| `lang/` | — | 占位 |

## 启动

```bash
python -m http.server 8082
# http://localhost:8082/
```

## 与 JS 版的区别

WASM 版运行性能远优于 JS 版（预编译字节码，无 JIT 开销），但体积略大。适合现代浏览器。
