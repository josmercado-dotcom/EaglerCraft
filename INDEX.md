# MCJS 本地镜像集（全版本）

按 mcjs.cc 官网全站清单镜像的浏览器版 Minecraft（Eaglercraft 系）版本，纯静态文件，统一 HTTP 服务按路由访问。

## 统一服务

```bash
cd C:\Users\Administrator\Desktop\MCJS
python server.py 8080          # 带 COOP/COEP 头（WASM-GC/WebGPU 必需）
# 浏览器打开 http://localhost:8080/
```

> 单文件版（1.16.5/1.21.11/26.1.2）必须走 `server.py` 而非 `python -m http.server`，否则 `SharedArrayBuffer` 不可用导致无法启动。

## 版本总览（18 个）

### 一、MCJS 优化版（推荐，中文）
| 路由 | 版本 | 技术 | 体积 | 联机 |
|------|------|------|------|------|
| `/1.8.8/` | EaglercraftX 1.8.8 JS u53 | TeaVM→JS | 21MB | 单机/局域网/远程 |
| `/1.8.8wasm/` | EaglercraftX 1.8.8 WASM u53 | TeaVM→WASM | 10MB | 同上 |
| `/1.12.2/` | Eaglercraft 1.12.2 JS u2 | TeaVM→JS | 28MB | 仅单机 |
| `/1.12.2wasm/` | Eaglercraft 1.12.2 WASM u2 | TeaVM→WASM | 16MB | 仅单机 |

### 二、最新测试版
| 路由 | 版本 | 技术 | 体积 | 备注 |
|------|------|------|------|------|
| `/1.12.2u3wasm/` | Eaglercraft 1.12.2 WASM u3 | WASM | 18MB | 新增导出世界+远程联机 |
| `/1.16.5.html` | Eaglercraft 1.16.5 WASM u2 beta | WASM 单文件 | 51MB | 性能低，需高性能电脑 |
| `/1.21.11.html` | Eaglercraft 1.21.11 WASM u1 beta | WASM 单文件 | 31MB | 特别卡 |
| `/26.1.2.html` | Eaglercraft 26.1.2 u0-1.2 | WASM-GC+WebGPU 单文件 | 46MB | 需 Chrome/Edge 113+ |

### 三、模组整合包（1.6.4 Forge）
| 路由 | 整合包 | 技术 | 体积 |
|------|--------|------|------|
| `/modpack/lite/` | Lite 轻量 | WASM | 8MB |
| `/modpack/tech/` | Tech 硬核科技 | WASM | 10MB |
| `/modpack/skyfactory/` | Skyfactory 天空工厂 | WASM | 8MB |
| `/modpack/magic/` | Magic 神奇魔法 | WASM | 7MB |

### 四、旧版（仅英文，怀旧）
| 路由 | 版本 | 技术 | 体积 |
|------|------|------|------|
| `/1.6.4/` | Eaglercraft 1.6.4 JS | TeaVM→JS | 15MB |
| `/1.5.2/` | Eaglercraft 1.5.2 JS SP2 | TeaVM→JS | 13MB |
| `/1.2.5/` | Eaglercraft 1.2.5 JS | TeaVM→JS | 17MB |

### 五、远古版（自包含 HTML）
| 路由 | 版本 | 技术 | 体积 |
|------|------|------|------|
| `/legacy/beta1.7.3/` | Eaglercraft Beta 1.7.3 | 内联 JS | 16MB |
| `/legacy/beta1.3/` | Eaglercraft Beta 1.3 | 内联 JS | 4.5MB |
| `/legacy/alpha1.2.6/` | Eaglercraft Alpha 1.2.6 | 内联 JS | 8.6MB |

## 文件结构

```
MCJS/
├── server.py               统一 HTTP 服务（带 COOP/COEP 头）
├── INDEX.md               本导航
├── 1.8.8/ 1.8.8wasm/      优化版 JS/WASM
├── 1.12.2/ 1.12.2wasm/ 1.12.2u3wasm/
├── 1.16.5.html 1.21.11.html 26.1.2.html   测试版单文件
├── modpack/{lite,tech,skyfactory,magic}/
├── 1.6.4/ 1.5.2/ 1.2.5/                  旧版 JS
└── legacy/{beta1.7.3,beta1.3,alpha1.2.6}/  远古版内联
```

## 技术栈说明

- **JS 版**：`classes.js`（TeaVM 编译）+ `assets.epk`（资源包，魔数 `EAGP`）
- **WASM 版**：`bootstrap.js`（加载器）+ `assets.epw`（资源包，魔数 `EAG$WASM`，内含 loader.js / loader.wasm）
- **单文件版**：所有代码与资源 base64 内联进一个 HTML，需 `SharedArrayBuffer` → 必须 `server.py`
- **远古版**：游戏代码内联在 `index.html`，无需额外文件

## 注意事项

- 存档：IndexedDB 本地，清缓存 = 丢档
- 联机：WebSocket P2P relay（lax1dude / MCJS 公益服务器）
- 测试版/模组包/旧版/远古版：仅英文，强制切中文会崩溃
- 高版本（1.16.5+/26.1.2）性能要求高，建议高性能电脑 + Chrome/Edge
- 详细说明见各子目录 `README.md`
