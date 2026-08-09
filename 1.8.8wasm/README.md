# MCJS 1.8.8 WASM — 本地镜像

镜像源：`https://mirror.mcjs.cc/1.8.8wasm/`（原站持续 RST，本镜像改用 `play.mcjs.144449.xyz` 同步内容，结构与文件字节相同）

## 文件清单

| 文件 | 大小 | 作用 |
|------|------|------|
| `index.html` | 6.4 KB | 入口：内嵌 `eaglercraftXOpts` 配置（中文 UI、联机 relay 列表），引用 `bootstrap.js` |
| `bootstrap.js` | 7.8 KB | 加载器：下载并校验 `assets.epw`，从中解析出 splash、loader.js、loader.wasm 三个内嵌组件 |
| `assets.epw` | 10.09 MB | 加密资源包（Eaglercraft 私有格式，magic `0x24554167 0x4D534157`）。内含：splash 图、loader.js、loader.wasm、游戏材质/声音/语言数据 |
| `lang/` | — | 占位目录（语言包已打包在 EPW 内） |

## 运行方式

EPW 加载器会发起跨域 fetch 并使用 WebAssembly/Web Worker，必须用 HTTP 协议访问，**不能直接 `file://` 打开**。

```bash
# 任选一种本地静态服务方式
cd "C:/Users/Administrator/Desktop/MCJS/1.8.8wasm"
python -m http.server 8080
# 浏览器打开 http://localhost:8080/
```

## 关键技术细节

- **后端**：纯静态，无服务器
- **存档**：浏览器 IndexedDB（单机），跨标签页/设备不同步
- **联机**：通过 WebSocket 连接公益 relay（`relay.deev.is` / `relay.lax1dude.net` / `relay.shhnowisnottheti.me` / `relay.mcjs.link`），P2P 中继
- **图标**：使用 `https://mcjs.cc/favicon.png`（外链，未本地化；如需离线运行可下载替换为相对路径 `favicon.png`）
- **页面分析**：Cloudflare Pages Analytics beacon（页面尾部，外链，可忽略）