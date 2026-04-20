# -*- coding: utf-8 -*-
# ANOVA-test för Lighthouse-resultat
# Jämför React vs Vanilla JS prestanda

import scipy.stats as stats
import numpy as np

# Vanilla JS data (Test 1-10)
vanilla_performance = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
vanilla_lcp = [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.4, 0.4, 0.4, 0.4]
vanilla_tbt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
vanilla_cls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
vanilla_speed = [0.2, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3]

# React data (Test 11-20)
react_performance = [95, 95, 94, 94, 94, 94, 95, 94, 95, 94]
react_lcp = [1.5, 1.4, 1.5, 1.5, 1.5, 1.5, 1.4, 1.5, 1.4, 1.4]
react_tbt = [20, 30, 40, 20, 30, 40, 20, 30, 30, 20]
react_cls = [0.001, 0.004, 0.001, 0.001, 0.004, 0.001, 0.004, 0.004, 0.004, 0.004]
react_speed = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 1.2]

print("ANOVA-TEST: React vs Vanilla JavaScript\n")

# Performance Score
print("1. Performance Score")
print(f"   Vanilla JS medelvärde: {np.mean(vanilla_performance):.2f}")
print(f"   React medelvärde: {np.mean(react_performance):.2f}")
f_stat, p_value = stats.f_oneway(vanilla_performance, react_performance)
print(f"   F-statistik: {f_stat:.4f}")
print(f"   P-värde: {p_value:.6f}\n")

# LCP
print("2. LCP (Largest Contentful Paint)")
print(f"   Vanilla JS medelvärde: {np.mean(vanilla_lcp):.2f} s")
print(f"   React medelvärde: {np.mean(react_lcp):.2f} s")
f_stat, p_value = stats.f_oneway(vanilla_lcp, react_lcp)
print(f"   F-statistik: {f_stat:.4f}")
print(f"   P-värde: {p_value:.10f}\n")

# TBT
print("3. TBT (Total Blocking Time)")
print(f"   Vanilla JS medelvärde: {np.mean(vanilla_tbt):.1f} ms")
print(f"   React medelvärde: {np.mean(react_tbt):.1f} ms")
f_stat, p_value = stats.f_oneway(vanilla_tbt, react_tbt)
print(f"   F-statistik: {f_stat:.4f}")
print(f"   P-värde: {p_value:.10f}\n")

# CLS
print("4. CLS (Cumulative Layout Shift)")
print(f"   Vanilla JS medelvärde: {np.mean(vanilla_cls):.4f}")
print(f"   React medelvärde: {np.mean(react_cls):.4f}")
f_stat, p_value = stats.f_oneway(vanilla_cls, react_cls)
print(f"   F-statistik: {f_stat:.4f}")
print(f"   P-värde: {p_value:.10f}\n")

# Speed Index
print("5. Speed Index")
print(f"   Vanilla JS medelvärde: {np.mean(vanilla_speed):.2f} s")
print(f"   React medelvärde: {np.mean(react_speed):.2f} s")
f_stat, p_value = stats.f_oneway(vanilla_speed, react_speed)
print(f"   F-statistik: {f_stat:.4f}")
print(f"   P-värde: {p_value:.10f}\n")

print("Not: P-värde < 0.05 indikerar statistiskt signifikant skillnad")
