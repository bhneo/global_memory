---
id: "source_e6608d8f849ad472bbd95143"
type: "source"
status: "captured"
title: "终于有人来挑战PI的flow matching的叙事了"
created_at: "2026-07-16T11:06:01+08:00"
updated_at: "2026-07-16T11:06:01+08:00"
aliases: []
tags: []
domains: []
confidence: "unknown"
source_ids: []
relations: []
source_kind: "wechat"
original_title: "终于有人来挑战PI的flow matching的叙事了"
author: "Marilyn Liu"
original_locator: "https://mp.weixin.qq.com/s?__biz=Mzk2NDg4MDcwNA==&mid=2247494112&idx=1&sn=9fd98185a671014b582d10693d2e8b65&chksm=c5297df976d2412516dfb91999848d872a34416a0ebf5c26e741f5fa09d42fa75fe2dc3ad1ca&mpshare=1&scene=24&srcid=0703RRlaGoqP0UphyjffqyWl&sharer_shareinfo=6770ca3be0825272c64c8438dc9bd5f8&sharer_shareinfo_first=7e30aadce42f5cd33036ea29ba18bc2b#rd"
canonical_locator: "https://mp.weixin.qq.com/s?__biz=Mzk2NDg4MDcwNA%3D%3D&idx=1&mid=2247494112&sn=9fd98185a671014b582d10693d2e8b65"
captured_at: "2026-07-16T11:06:01+08:00"
published_at: "2026-06-01T19:57:35+08:00"
content_sha256: "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228"
content_id: "content_4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228"
raw_content_path: "vault/raw/objects/sha256/4a/76/4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228"
save_reason: "用户导入：微信文章"
import_method: "cli-wechat"
processing_status: "inbox"
content_type: "text/html; charset=UTF-8"
mime_type: "text/html"
original_filename: ""
display_extension: ".html"
source_family_id: "source_family_e6608d8f849ad472bbd95143"
version_number: 1
previous_version_id: null
---

# 终于有人来挑战PI的flow matching的叙事了

> 原始内容：[vault/raw/objects/sha256/4a/76/4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228](../objects/sha256/4a/76/4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228)

## 来源版本

- Family：`source_family_e6608d8f849ad472bbd95143`
- Version：`1`
- Previous：`none`

## 保存理由

用户导入：微信文章

## 内容预览

终于有人来挑战PI的flow matching的叙事了 原创 Marilyn Liu Marilyn Liu 具身纪元 在小说阅读器读本章 去阅读 在小说阅读器中沉浸阅读 通用机器人要的VLA模型，天生要同时干两件性质相反的事。语言是离散的下一个 token 预测，动作是连续的实时控制，怎么让这两种信号在同一个模型里共处，几乎定义了每一种 VLA 的架构选择。 PI 推出了π0，几乎为Flowmatching的主流定了调， 一个预训练视觉-语言模型管理解，一个单独训练的流匹配专家管出动作 。 但是否flow matching是这件事的唯一正确的解法，其实并不是自明的。 我读了星海图（Galaxea） G0.5 技术报告，发现它在挑战这种行业主流，把动作生成的权力从外挂专家手里收回到VLM模型自己身上，用一套统一权重、一个 transformer 解码器，在同一条自回归序列里同时生成推理和动作。 要看懂这篇技术报告的问题意识，得先回到语言和动作这对矛盾，以及行业是如何处理的。 自回归先行，为什么流匹配后来居上 这波具身发展的起点，其实是由VLM点燃的。VLM极其强大，可以针对未见的场景做出规划，具备直接输出动作的潜力。RT-2、OpenVLA、π0-FAST 都把连续动作离散成 token，附到语言词表后面，让视觉-语言模型像预测下一个字一样预测下一个动作。 VLM预训练得来的世界知…
