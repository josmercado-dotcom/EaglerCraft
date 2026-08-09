# MCJS 1.8.8 JS 版 — 本地镜像

镜像源：`mcjs-mirror-test.144449.xyz/1.8.8/`

技术：TeaVM 将 Minecraft Java 1.8.8 字节码编译为 JavaScript（无 Wasm），WebGL 渲染。

## 文件清单

| 文件 | 大小 | 作用 |
|------|------|------|
| `index.html` | 6.3 KB | 入口：用户许可协议弹窗 + EaglercraftOpts |
| `classes.js` | 14.2 MB | 游戏主体 — TeaVM 编译的 JS 代码 |
| `assets.epk` | 6.9 MB | 加密资源包（魔法数 OK） |
| `lang/` | — | 占位（语言资源从 EPK 内取） |

## 启动

```bash
python -m http.server 8080
# http://localhost:8080/
```

## 与 WASM 版的区别

JS 版体积小（整体 22MB vs WASM 版 10MB），但加载慢 — classes.js 是 14MB 纯 JS 文本，首次执行 JIT 编译较慢。适合低性能设备或不支持 WASM-GC 的旧浏览器。
