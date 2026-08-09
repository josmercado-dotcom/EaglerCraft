# MCJS 1.12.2 JS 版 — 本地镜像

镜像源：`playmcjscc.pages.dev/1.12.2/`（Cloudflare Pages）

技术：TeaVM 将 Minecraft Java 1.12.2 字节码编译为 JavaScript（u32 版），WebGL 渲染。此为 EaglercraftX 1.12.2 完整移植。

## 文件清单

| 文件 | 大小 | 作用 |
|------|------|------|
| `index.html` | 2.8 KB | 入口：`eaglercraftXOpts`（assets.epk, lang/，联机 relay 配置）|
| `classes.js` | 13.8 MB | 游戏主体 — TeaVM u32 编译的 EaglercraftX 1.12.2 JS 代码 |
| `assets.epk` | 13.9 MB | 加密资源包（魔法数 OK） |
| `lang/` | — | 占位 |

## 启动

```bash
python -m http.server 8081
# http://localhost:8081/
```

## 特点

- 支持 MC 1.12.2 全部特性（海洋更新 + 色彩更新），功能完整体量也更大（整体 28MB）
- 此站托管在 Cloudflare Pages 且有 CF Analytics beacon（页面尾部），本地镜像已剥离该外链
- 联机配置默认走 3 个 relay（lax1dude + ayunami）随机选一个
