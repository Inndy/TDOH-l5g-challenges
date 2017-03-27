# l5g challenges

## lag

簡單的 stream cipher，但是有效 state 只有 8bits 所以可以破解

## leg

N 元一次方程式，高斯消去法就可以解，或是找 solver

這裡我用了 z3 SMT solver，有個坑是 BitVec 解不出來，一定要用 Int

## lig

LSB 藏資料，exif data 有提示，找到網頁只後透過 google 找到維基百科的原文，填入缺少的字就會解密 flag

## log

sqlmap blind boolean-based SQL injection 攻擊流量記錄，binary search 分析

## lug

upx 包裝的 ELF 執行檔，有 linux 環境就可以拿到 flag，東西會寫到 `/tmp/.flag`，也可以 gdb 後 break 在 syscall 然後 dump memory

## adr\_challs

這些是 Adr 出的題目，不過我也都解完了，順手留個解答

## ncu-nos-wargame

中央大學網路開源社準備的 wargame，但是 .git 沒關所以備份下來了
