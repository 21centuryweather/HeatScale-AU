# HeatScale-AU

## Proposed research title

**Sensitivity of Physically Based Wet-Bulb Globe Temperature and Occupational Heat-Risk Estimates to Atmospheric Reanalysis and Spatial Resolution Across Australia**

**Short project name:** HeatScale-AU

---

## 1. Project overview

HeatScale-AU will investigate whether the atmospheric dataset used to describe Australian weather materially changes estimates of human heat stress and downstream occupational heat-risk decisions.

The study is inspired by Prein et al. (2026), who calculated physically based Wet-Bulb Globe Temperature (WBGT) from ERA5 and the approximately 4-km CONUS404 regional simulation over North America. Their analysis linked hourly WBGT to extreme heat, threshold exceedance, nighttime heat stress, heatwave duration, potential work capacity, population exposure, and the meteorological drivers of WBGT change.

The Australian study will not simply reproduce the North American analysis. Instead, it will use the Australian reanalysis hierarchy

**ERA5 (~30 km) → BARRA-R2 (~12 km) → BARRA-C2 (~4.4 km)**

to ask a more focused question:

> **How strongly do atmospheric dataset choice and spatial scale propagate through a physically based heat-stress calculation into decision-relevant estimates of occupational heat risk across Australia?**

The central scientific issue is not whether a finer grid produces a more detailed map. The issue is whether differences in temperature, humidity, wind, pressure, and radiation among atmospheric products are large enough, and sufficiently nonlinear, to alter WBGT extremes, threshold exceedance, heat-risk classification, and potential workability.

---

## 2. Research gap

Australian research already contains several parts of this problem.

- Physically based WBGT has been applied to Australian climate conditions.
- WBGT has been linked to labour capacity and predicted heat strain.
- Australian occupational heat exposure has been studied extensively.
- BARRA has been used for high-resolution Australian meteorology and thermal-stress applications.
- BARRA-R2 and BARRA-C2 have been evaluated against observations and ERA5.
- Australian heatwave conclusions have been shown to depend on the underlying observational dataset.
- High-resolution, hourly and radiation-aware thermal-stress modelling has been demonstrated in Australia.

However, the literature reviewed for this project did **not identify a published Australian study that applies the same physically based Liljegren/Kong-Huber WBGT implementation to concurrent hourly ERA5, BARRA-R2 and BARRA-C2 meteorological fields and then quantifies how differences in atmospheric dataset and effective spatial resolution propagate into WBGT extremes, threshold exceedance or classification, and occupational workability estimates.**

This is the narrow research gap addressed by HeatScale-AU.

### Claims that should NOT be made

The study should not claim to be:

- the first Australian WBGT study;
- the first physically based WBGT study in Australia;
- the first use of BARRA in Australian heat research;
- the first Australian WBGT/labour-capacity study;
- the first ERA5-versus-BARRA comparison;
- proof that BARRA-C2 is more accurate simply because it has a 4.4-km grid.

The novelty is instead the **propagation of meteorological dataset and spatial-scale uncertainty through the same nonlinear physical WBGT calculation into decision-relevant heat-risk outcomes**.

---

# 3. Literature review

## 3.1 Why physically based WBGT is the appropriate heat-stress metric

Heat stress cannot be represented by air temperature alone. Human heat exchange with the environment depends on air temperature, atmospheric moisture, wind, and radiant heat. WBGT combines these effects through natural wet-bulb temperature, black-globe temperature, and dry-bulb temperature.

Liljegren et al. (2008) developed a physically based outdoor WBGT model using fundamental heat- and mass-transfer equations rather than site-specific empirical regression. The model separately solves natural wet-bulb and globe temperatures from standard meteorological observations and was validated against measured WBGT, achieving errors of less than approximately 1 °C under the conditions considered. Their work is particularly relevant to HeatScale-AU because it also demonstrated that spatial variability in WBGT, especially variability in globe temperature associated with cloud and solar exposure, can be comparable to or larger than model-prediction uncertainty. This directly motivates investigating the effect of spatial resolution on WBGT.

Kong and Huber (2022) showed why simplified WBGT formulations are unsuitable for the proposed study. Using ERA5, they compared explicitly calculated Liljegren WBGT with common approximations such as simplified WBGT and the Environmental Stress Index. The approximations showed systematic biases, and both could underestimate extreme heat stress. Errors were strongly state dependent, with solar radiation, wind, temperature, and humidity interacting to determine the magnitude and sign of the bias. Importantly, the study demonstrated that errors in WBGT can propagate into much larger errors in estimated labour productivity. Kong and Huber also warned against calculating nonlinear heat-stress metrics from daily or monthly averaged meteorology and recommended using high-temporal-resolution inputs.

This is fundamental to HeatScale-AU. If WBGT is calculated using hourly ERA5, BARRA-R2, and BARRA-C2 data, differences among those atmospheric datasets are allowed to propagate through the complete physical calculation instead of being obscured by a simplified temperature-humidity approximation.

Kong and Huber (2025) subsequently developed an analytical sensitivity framework for WBGT. The framework expresses changes in WBGT in terms of changes in air temperature, specific humidity, surface pressure, wind-related effects, and solar-radiation effects. Because the sensitivity coefficients vary with the background climatic state, the same meteorological difference can have a different effect on WBGT in humid tropical, hot-arid, coastal, and temperate environments. This provides a natural framework for diagnosing *why* ERA5, BARRA-R2, and BARRA-C2 disagree rather than merely describing their differences.

Together, Liljegren et al. (2008), Kong and Huber (2022), and Kong and Huber (2025) establish the physical and methodological basis for the project:

1. use explicit physics-based WBGT;
2. retain hourly meteorological covariability;
3. analyse the upper tail and threshold crossings, not only mean bias;
4. diagnose contributions from individual meteorological variables.

---

## 3.2 Prein et al. (2026) as the methodological starting point

Prein et al. (2026) provides the closest international methodological analogue. They calculated physically based WBGT from hourly ERA5 and the approximately 4-km CONUS404 simulation over North America. CONUS404 dynamically downscales ERA5, making the comparison conceptually similar to the Australian hierarchy in which BARRA2 is nested within ERA5 and BARRA-C2 is nested within BARRA-R2.

Prein et al. examined annual maximum WBGT, threshold exceedance, nighttime heat stress, heatwave characteristics, potential work capacity, population exposure, and the meteorological drivers of WBGT change. Their high-resolution simulation added strong spatial structure associated with topography and land use that was not evident in ERA5. In some areas, differences were large enough to change the direction or magnitude of the inferred WBGT response.

The study also demonstrates why threshold analysis can behave very differently from continuous WBGT analysis. Locations already close to critical WBGT levels experienced disproportionately large changes in threshold-exceedance frequency for relatively modest shifts in WBGT. This is directly relevant to HeatScale-AU: a difference of less than 1 °C between two atmospheric products may appear small in a conventional bias map but may move many hours across an occupational reference threshold.

Prein et al. used U.S. military flag thresholds of approximately 27.8 °C, 29.4 °C, and 32 °C and a separate ISO/NIOSH-based workability calculation. These flag values are useful for reproducing their analysis and international comparison, but they should not be described as Australian legal stop-work thresholds.

The Australian study will therefore adapt the **analysis logic** of Prein et al. rather than copy the study literally. The historical reanalysis comparison and spatial-scale sensitivity will be the primary focus, while future pseudo-global-warming analysis is outside the initial scope.

---

## 3.3 Existing Australian WBGT research

Australian WBGT research means that HeatScale-AU must make a narrow novelty claim.

Newth and Gunasekera (2018) analysed projected global and regional WBGT changes using CMIP5 climate simulations and identified northern Australia as one of the regions expected to experience disproportionate increases in heat stress. This work establishes long-standing concern about Australian WBGT under climate change but does not examine hourly reanalysis choice or kilometre-scale atmospheric representation.

Hall and colleagues subsequently developed physically based Australian WBGT mapping. Hall and Horta (2023) describe the earlier Hall et al. (2022) study as applying the accurate Liljegren method over Australia under RCP4.5 and RCP8.5 scenarios. That earlier analysis used two prescribed wind-speed scenarios and clear atmospheric conditions, meaning that real hourly covariability of wind, cloud, shortwave radiation, longwave radiation, temperature, and moisture was not represented.

Hall and Horta (2023) extended this work by explicitly manipulating shade and airflow. They demonstrated substantial spatial variation in the cooling effect of shade and wind and linked WBGT to labour capacity. A 90% reduction in incident radiation lowered WBGT by approximately 2–6 °C depending on location, while the effect of wind became weaker in the hottest environments. Their study is important because it demonstrates that radiation and wind can materially alter WBGT and downstream labour-capacity estimates. However, the purpose was to test environmental interventions, not atmospheric dataset uncertainty.

Hunt et al. (2023) further linked Australian heat environments to worker physiology. Using climate scenarios for Darwin, Townsville, Tom Price, Griffith, Port Macquarie, and Clare, they applied the ISO 7933 Predicted Heat Strain model to estimate safe work duration before a core-temperature threshold of 38 °C or 5% body-mass sweat loss was reached. Predicted safe work durations declined under future warming, with particularly large relative reductions in some southeastern locations. This provides a strong precedent for translating meteorological heat exposure into physiologically meaningful occupational endpoints.

These studies show that HeatScale-AU cannot claim novelty from WBGT itself or from linking WBGT to work capacity. Its contribution is to determine whether **the atmospheric dataset feeding the calculation changes those conclusions**.

---

## 3.4 Australian occupational heat-stress evidence

Jay and Brotherhood (2016) reviewed 29 reports covering Australian occupational environments in mining, agriculture, construction, emergency services, military activities, and related work settings. WBGT was the most commonly reported environmental heat measure in the reviewed studies. However, the review also emphasised that similar WBGT values can arise from very different combinations of temperature, humidity, radiation, and airflow and recommended measuring individual environmental components where possible.

This point is especially important for HeatScale-AU. ERA5 and BARRA may generate similar WBGT values for different physical reasons, or their errors in individual meteorological variables may compensate. Conversely, relatively small errors in several meteorological components may reinforce each other and produce a significant WBGT difference.

The Australian occupational literature also shows that environmental hazard alone does not determine physiological strain. Metabolic heat production, work intensity, clothing, acclimatisation, hydration, pacing, and individual characteristics are important. Consequently, HeatScale-AU should describe its downstream metric as **potential work capacity**, **modelled workability**, or **allowable exposure duration**, rather than observed economic productivity.

The broader Australian work-health-and-safety review by Wuersch et al. (2023) similarly identifies heat and extreme weather as major climate-related workplace hazards while showing that evidence remains uneven across occupations and outcomes.

---

## 3.5 High-resolution Australian thermal-stress modelling

Weeding et al. (2024) provides a useful Australian demonstration of why both spatial and temporal resolution matter. Their Hobart study produced hourly metre-scale projections of thermal stress using multivariate bias-corrected climate data, BARRA-TA as a reference dataset, explicit radiation modelling, and the Universal Thermal Climate Index rather than WBGT.

Although the index and objective differ from HeatScale-AU, the study is methodologically relevant for three reasons.

First, it emphasises that thermal-stress variables vary strongly on hourly timescales. Second, it shows the importance of preserving relationships among multiple meteorological variables rather than treating them independently. Third, it demonstrates that fine spatial structure can change whether conditions are interpreted as safe or hazardous.

HeatScale-AU addresses a complementary scale question. Instead of downscaling from kilometres to metres within one city, it asks whether moving from a global reanalysis to 12-km and 4.4-km Australian regional products changes nationally relevant WBGT and occupational-risk estimates.

---

## 3.6 Australian heat-health evidence

Amoatey et al. (2025) reviewed 64 Australian heat-health studies published between 2007 and 2023. Most were epidemiological studies focused on mortality, hospital admissions, emergency presentations, ambulance callouts, or heat-vulnerability indices. The review found strong evidence of adverse heat-health effects but also identified a need for finer-scale spatial heat-health assessment and better coverage of non-urban and remote areas.

This literature establishes the public-health importance of heat exposure but also shows that most Australian health studies do not investigate how the choice of atmospheric reanalysis changes a physically based heat-stress exposure metric.

Perkins-Kirkpatrick et al. (2026) provides a particularly useful event-scale case study. Their physiology-based HEAT-Lim analysis included the January 2019 Mount Isa heat event and used ERA5 to characterise the city-scale heatwave. The study showed that extremely hot, dry conditions can be physiologically dangerous even when humidity is not exceptionally high. Mount Isa is therefore a strong candidate for a HeatScale-AU event study because it provides an independently identified Australian heat-stress event for which an ERA5-based conclusion can be compared with BARRA-R2 and BARRA-C2.

---

## 3.7 Evidence that the underlying dataset can change Australian heat conclusions

Reddy, Perkins-Kirkpatrick, and Sharples (2021) provides one of the strongest conceptual precedents for HeatScale-AU. They analysed Australian heatwave metrics using AWAP, SILO, and ACORN-SATv2 and found that local heatwave trends could differ noticeably among observational products. Their discussion attributes these differences to small variations in the underlying temperature data, gridding methods, station density, and homogenisation, which then interact with threshold-based heatwave definitions.

This is directly analogous to the proposed WBGT problem. Threshold-based metrics can amplify relatively small differences in the underlying climate fields.

The implication is that the HeatScale-AU hypothesis should not be framed as “higher resolution must change the result.” A stronger and falsifiable formulation is:

> **Under which Australian climate regimes, spatial scales, and decision thresholds does atmospheric dataset choice materially alter a heat-stress conclusion, and where are the conclusions robust?**

Both sensitivity and robustness are scientifically useful outcomes.

---

## 3.8 BARRA2 and the Australian reanalysis hierarchy

The Bureau of Meteorology's BARRA2 system makes this experiment possible.

Su et al. (2025) describe BARRA2 as a regional atmospheric reanalysis nested within ERA5 and extending from 1979 to near present. BARRA-R2 has a horizontal grid spacing of approximately 12 km over the wider Australasian domain, while BARRA-C2 provides an approximately 4.4-km convection-permitting configuration over Australia.

BARRA-R2 performs regional data assimilation, including four-dimensional variational atmospheric assimilation and land-surface assimilation. BARRA-C2 is fundamentally different. Bureau Research Report 097 states that BARRA-C2 is dynamically downscaled from BARRA-R2 and does not perform its own convective-scale data assimilation. The additional information in BARRA-C2 therefore arises primarily from finer horizontal resolution, different model physics, and improved representation of land surface, terrain, and convective-scale processes.

This distinction has major implications for interpretation:

**ERA5, BARRA-R2, and BARRA-C2 are not independent estimates.**

The hierarchy is approximately:

**ERA5 → BARRA-R2 → BARRA-C2**

Consequently, the proposed comparison should be described as sensitivity across an atmospheric reanalysis/downscaling hierarchy, not as an ensemble of independent products.

BARRA-C2 should also not be treated as observational truth. The BARRA2 assessment states that C2 inherits errors and biases from BARRA-R2, and the two BARRA2 systems do not always outperform ERA5. Examples include some inland 10-m wind and tropical-cyclone-position errors. BARRA2 also exhibits changes in quality around approximately 2000, with greater uncertainty in earlier years when observational constraints were weaker. This suggests that HeatScale-AU should consider a primary analysis from approximately 2000 onward, with the full 1979-present record treated as a sensitivity or secondary analysis if long-term trends are included.

The BARRA-C2 technical report also confirms that high-frequency surface and near-surface meteorological output is archived, including the classes of variables required for physically based WBGT. However, the exact NCI variable names, units, accumulation conventions, timestamps, and radiation definitions must be audited before any WBGT calculation is performed.

---

# 4. Research questions

## RQ1. Continuous heat-stress exposure

**How do hourly physically based WBGT estimates from ERA5, BARRA-R2, and BARRA-C2 differ across Australia, particularly in the upper tail of the distribution and during extreme events?**

Primary quantities:

- hourly WBGT;
- seasonal and annual means;
- 95th, 99th, and 99.5th percentiles;
- annual maximum hourly WBGT;
- spatial structure of extreme WBGT.

## RQ2. Decision sensitivity

**How often does atmospheric dataset choice change whether the same place and hour exceeds an occupationally relevant WBGT reference level?**

Primary quantities:

- exceedance hours;
- consecutive exceedance duration;
- classification disagreement rate;
- direction of disagreement;
- pairwise confusion matrices.

## RQ3. Spatial resolution and nonlinear aggregation

**How much of the apparent difference among datasets arises from loss of sub-grid meteorological variability and nonlinear aggregation, rather than from differences among atmospheric modelling systems?**

The key controlled experiment will compare:

1. WBGT calculated from native 4.4-km BARRA-C2 meteorology;
2. WBGT calculated after BARRA-C2 meteorological inputs are aggregated to a coarser grid;
3. BARRA-C2 WBGT calculated first at 4.4 km and then spatially aggregated.

Because WBGT is nonlinear,

`WBGT(mean meteorology)` is not generally equal to `mean(WBGT from fine-scale meteorology)`.

A second nonlinearity appears when a threshold is applied. This means a coarse-grid average may appear accurate while failing to represent local threshold exceedance.

## RQ4. Physical drivers of disagreement

**Which meteorological differences are responsible for WBGT disagreement among ERA5, BARRA-R2, and BARRA-C2 in different Australian climate regimes?**

The Kong and Huber sensitivity framework will be used to examine contributions from:

- air temperature;
- specific humidity or equivalent moisture variable;
- wind;
- surface pressure;
- shortwave radiation;
- longwave/radiative effects.

## RQ5. Occupational consequence

**Do atmospheric-data differences materially alter potential work capacity, allowable exposure duration, or other occupationally relevant heat-management indicators?**

These outputs must be described as modelled potential effects, not realised economic productivity.

---

# 5. Hypotheses

**H1.** Differences among ERA5, BARRA-R2, and BARRA-C2 will be more pronounced for extreme WBGT and threshold-exceedance duration than for median WBGT.

**H2.** Relatively small differences in continuous WBGT will produce disproportionately larger differences in threshold-based classifications where the local WBGT distribution lies close to a decision threshold.

**H3.** BARRA-C2 will resolve greater fine-scale spatial variance and local extremes than coarser products, particularly in coastal, topographic, and strong humidity/wind-gradient environments, but it will not necessarily have lower observational error everywhere.

**H4.** Dataset sensitivity will be largest where cloud/radiation, sea-breeze circulations, coastal moisture gradients, topographic flow, or local wind regimes are incompletely represented at coarse resolution.

**H5.** WBGT calculated after aggregating meteorological inputs will differ from WBGT calculated at 4.4 km and aggregated afterward because WBGT and the subsequent threshold operation are nonlinear.

---

# 6. What will be done in this research

## Phase 1. Reproduce and audit the WBGT calculation

- Use the physically based Liljegren/Kong-Huber Python implementation.
- Reproduce selected calculations from the Prein workflow.
- Verify the final published threshold definitions rather than assuming all values in the Prein GitHub repository match the final paper.
- Build unit tests for known meteorological conditions.

## Phase 2. Build the ERA5/BARRA variable crosswalk

For each product, identify and verify:

- near-surface air temperature;
- specific or relative humidity;
- surface pressure;
- zonal and meridional near-surface wind;
- downward shortwave radiation;
- upward/reflected shortwave radiation where used;
- downward longwave radiation;
- upward longwave radiation where used;
- latitude, longitude, and elevation;
- time coordinate and local-time conversion.

For each variable, record:

- NCI/CDS variable name;
- units;
- height or level;
- instantaneous versus mean/accumulated quantity;
- timestamp convention;
- temporal resolution;
- missing-data treatment.

## Phase 3. Pilot event analysis

Before processing the entire Australian archive, perform proof-of-concept analyses for contrasting heat regimes.

Recommended cases include:

- **Mount Isa, January 2019**: hot-dry inland event independently highlighted by Perkins-Kirkpatrick et al. (2026);
- **Melbourne/southeastern Australia, January 2014**: major heatwave used in BARRA2 evaluation;
- **Darwin or Townsville**: humid tropical/coastal regime;
- optionally **Tom Price/Pilbara**: hot-dry mining environment.

For each case calculate ERA5, BARRA-R2, and BARRA-C2 WBGT and determine whether the differences are large enough to alter extreme values or threshold classifications.

## Phase 4. National historical analysis

If the pilot demonstrates meaningful signal, calculate hourly WBGT nationally over a common period.

A sensible primary analysis period may begin around **2000**, because BARRA2 documentation identifies quality changes around that time. A secondary/full-period analysis can assess 1979-present behaviour if appropriate.

Outputs will include:

- mean and percentile WBGT;
- annual maxima;
- seasonal cycles;
- threshold-exceedance hours;
- event duration;
- nighttime heat-stress metrics where justified;
- spatial patterns of disagreement.

## Phase 5. Controlled spatial-scale experiment

BARRA-C2 will be used to distinguish scale effects from simple native-dataset differences.

For a target coarse grid:

### A. Aggregate inputs first

`WBGT_A = f(mean(T), mean(q), mean(p), mean(U), mean(SW), mean(LW))`

### B. Calculate first, aggregate second

`WBGT_B = mean(f(T, q, p, U, SW, LW))`

The difference `WBGT_A - WBGT_B` quantifies the effect of nonlinear spatial aggregation within the BARRA-C2 field.

This experiment should be repeated at approximately BARRA-R2 and ERA5 scales.

## Phase 6. Decision-disagreement analysis

Define categorical disagreement between products rather than relying only on temperature bias.

For each grid cell and hour, determine whether two products assign the same heat-risk category or threshold state.

Key metrics:

- annual disagreement hours;
- fraction of time in disagreement;
- ERA5-lower-risk versus BARRA-C2-lower-risk cases;
- conditional probability of threshold crossing in one product but not another;
- disagreement during the most extreme days;
- differences in potential work capacity.

This will be one of the central decision-relevant outputs of the study.

## Phase 7. Physical attribution

Use the Kong-Huber framework and direct component analysis to determine whether disagreement is primarily caused by:

- temperature;
- humidity;
- wind;
- shortwave radiation/cloud;
- longwave radiation;
- pressure.

The attribution should be stratified by Australian climate regime.

## Phase 8. Evaluation against observations

BARRA-C2 must not be treated as truth.

Evaluation should use, where available:

1. direct measured WBGT;
2. physically reconstructed WBGT from collocated meteorological observations;
3. Bureau station temperature, humidity, wind, and pressure;
4. appropriate radiation observations.

Observation comparisons must acknowledge that some stations are assimilated into BARRA-R2, meaning they are not fully independent validation data.

---

# 7. Primary outputs

The study should prioritise the following outputs.

### Continuous quantities

- WBGT bias/difference;
- MAE/RMSE against observations where possible;
- upper percentiles;
- annual maximum;
- event maxima.

### Threshold and decision quantities

- exceedance hours;
- maximum consecutive exceedance duration;
- classification disagreement rate;
- confusion matrices;
- spatial fraction of a region changing classification.

### Occupational quantities

- potential work capacity;
- allowable exposure duration or PHS-based case-study metrics;
- workability during standard working hours.

Prein's U.S. military flag thresholds may be reproduced as an **international-comparison sensitivity analysis**, but they should not be presented as Australian statutory thresholds. Australian/ISO/AIOH-informed occupational scenarios should be used for the main interpretation.

---

# 8. Expected contribution

HeatScale-AU is expected to contribute in four ways.

1. **Dataset sensitivity:** quantify how much physically based Australian WBGT depends on ERA5, BARRA-R2, or BARRA-C2.

2. **Scale sensitivity:** determine whether kilometre-scale meteorological variability is lost when heat stress is calculated from coarser atmospheric fields.

3. **Decision sensitivity:** establish whether meteorological differences are large enough to change threshold classifications or workability estimates.

4. **Process understanding:** identify which meteorological variables cause disagreements across tropical humid, hot-arid, coastal, urban-adjacent, and complex-terrain environments.

The study will therefore move beyond the statement that “high-resolution data provide more detail.” It will test whether that detail is **decision relevant**.

---

# 9. Important methodological cautions

The following issues should be addressed explicitly in the analysis and manuscript.

1. **Resolution-model confounding:** ERA5, BARRA-R2, and BARRA-C2 differ in more than grid spacing.
2. **Nested dependence:** the products are not independent because BARRA2 is nested in ERA5 and C2 is nested in R2.
3. **BARRA-C2 is not truth:** finer resolution does not guarantee lower error.
4. **Temporal inhomogeneity:** BARRA2 quality changes around approximately 2000.
5. **Radiation conventions:** instantaneous, hourly mean, accumulated, upward/downward, and net fluxes must be handled correctly.
6. **Temporal alignment:** UTC, civil local time, solar time, and radiation interval definitions must be consistent.
7. **Wind height:** 10-m model wind is not identical to worker-level airflow.
8. **Urban/microclimate limitation:** a 4.4-km grid is still ambient kilometre-scale meteorology, not workplace microclimate.
9. **Threshold dependence:** conclusions may depend strongly on the occupational threshold and work intensity selected.
10. **Physiological heterogeneity:** clothing, metabolic rate, acclimatisation, fitness, hydration, and vulnerability modify actual risk.
11. **Work capacity is not economic productivity:** modelled workability should not be interpreted as observed financial loss.
12. **Observation dependence:** BARRA-R2 assimilates observations, complicating claims of fully independent station validation.
13. **Nonlinear interpolation:** regridding meteorology before WBGT calculation is not mathematically equivalent to regridding WBGT afterward.

---

# 10. Literature still recommended for the repository

The current `LITERATURE_REVIEW` tree contains the core methodological and Australian papers needed to start the project, but several important papers identified during the independent literature search are not visible in the supplied repository tree. They should be added before treating the review as complete:

1. **Hall, A., Horta, A., Khan, M. R., & Crabbe, R. A. (2022).** Spatial analysis of outdoor wet bulb globe temperature under RCP4.5 and RCP8.5 scenarios for 2041–2080 across a range of temperate to hot climates. *Weather and Climate Extremes, 35*, 100420. https://doi.org/10.1016/j.wace.2022.100420

2. **Nairn, J., Moise, A., & Ostendorf, B. (2022).** The impact of humidity on Australia's operational heatwave services. *Climate Services, 27*, 100315. https://doi.org/10.1016/j.cliser.2022.100315

3. **Palmer, G., Dargaville, R., Su, C.-H., et al. (2025).** Validation of BARRA2 and comparison with MERRA-2 and ERA5 using historical wind power generation. *Journal of Southern Hemisphere Earth Systems Science, 75*(1), ES24028. https://doi.org/10.1071/ES24028

4. **Cheung, K. K. W., Ji, F., Nishant, N., et al. (2025).** Comparison of BARRA and ERA5 in replicating mean and extreme precipitation over Australia. *Hydrology and Earth System Sciences, 29*, 3527–3543. https://doi.org/10.5194/hess-29-3527-2025

5. **Borg, M. A., Xiang, J., Anikeeva, O., et al. (2025).** Anomalous temperatures increase occupational injuries, illnesses and associated cost burden in Australia. *Urban Climate, 59*, 102307. https://doi.org/10.1016/j.uclim.2025.102307

6. **Ireland, A., Johnston, D., & Knott, R. (2023).** Heat and worker health. *Journal of Health Economics*, 102800. https://doi.org/10.1016/j.jhealeco.2023.102800

7. **Su, C.-H., & Yan, H. (2026).** Enhanced sub-daily temperatures from Australian atmospheric reanalysis. Bureau of Meteorology Research Report.

These studies are particularly important for the novelty argument because they establish the nearest Australian precedents in BARRA-based heat analysis, ERA5/BARRA sensitivity, occupational outcomes, and BARRA-R2/C2 evaluation.

---

# 11. Core references

Amoatey, P., Xu, Z., Odebeatu, C. C., Singh, N., Osborne, N. J., & Phung, D. (2025). Impact of extreme heat on health in Australia: a scoping review. *BMC Public Health, 25*, 522. https://doi.org/10.1186/s12889-025-21677-9

García-León, D., Casanueva, A., Standardi, G., Burgstall, A., Flouris, A. D., & Nybo, L. (2021). Current and projected regional economic impacts of heatwaves in Europe. *Nature Communications, 12*, 5807. https://doi.org/10.1038/s41467-021-26050-z

Grundstein, A., & Cooper, E. (2018). Assessment of the Australian Bureau of Meteorology wet bulb globe temperature model using weather station data. *International Journal of Biometeorology*. https://doi.org/10.1007/s00484-018-1624-1  
**Note:** despite the title, the empirical validation uses weather stations in Georgia, USA; it is methodological evidence rather than Australian empirical evidence.

Hall, A., & Horta, A. (2023). Broad Scale Spatial Modelling of Wet Bulb Globe Temperature to Investigate Impact of Shade and Airflow on Heat Injury Risk and Labour Capacity in Warm to Hot Climates. *International Journal of Environmental Research and Public Health, 20*, 6531. https://doi.org/10.3390/ijerph20156531

Hunt, A. P., Brearley, M., Hall, A., & Pope, R. (2023). Climate Change Effects on the Predicted Heat Strain and Labour Capacity of Outdoor Workers in Australia. *International Journal of Environmental Research and Public Health, 20*, 5675. https://doi.org/10.3390/ijerph20095675

Jay, O., & Brotherhood, J. R. (2016). Occupational heat stress in Australian workplaces. *Temperature, 3*(3), 394–411. https://doi.org/10.1080/23328940.2016.1216256

Kong, Q., & Huber, M. (2022). Explicit Calculations of Wet-Bulb Globe Temperature Compared With Approximations and Why It Matters for Labor Productivity. *Earth's Future, 10*, e2021EF002334. https://doi.org/10.1029/2021EF002334

Kong, Q., & Huber, M. (2025). A Linear Sensitivity Framework to Understand the Drivers of the Wet-Bulb Globe Temperature Changes. *Journal of Geophysical Research: Atmospheres, 130*, e2024JD042195. https://doi.org/10.1029/2024JD042195

Liljegren, J. C., Carhart, R. A., Lawday, P., Tschopp, S., & Sharp, R. (2008). Modeling the Wet Bulb Globe Temperature Using Standard Meteorological Measurements. *Journal of Occupational and Environmental Hygiene, 5*(10), 645–655. https://doi.org/10.1080/15459620802310770

Newth, D., & Gunasekera, D. (2018). Projected Changes in Wet-Bulb Globe Temperature under Alternative Climate Scenarios. *Atmosphere, 9*, 187. https://doi.org/10.3390/atmos9050187

Páscoa, P., Gouveia, C. M., Russo, A., & Ribeiro, A. F. S. (2022). Summer hot extremes and antecedent drought conditions in Australia. *International Journal of Climatology*. https://doi.org/10.1002/joc.7544

Perkins-Kirkpatrick, S. E., Gregory, C. H., Vanos, J. K., et al. (2026). Deadly heat stress conditions are already occurring. *Nature Communications*. https://doi.org/10.1038/s41467-026-70485-1

Prein, A. F., Kong, Q., Villarini, G., Done, J. M., Johnson, D. R., Wang, C., & Huber, M. (2026). Local drivers in accelerating North American heat stress. *Nature Communications, 17*, 6600. https://doi.org/10.1038/s41467-026-72795-w

Reddy, P. J., Perkins-Kirkpatrick, S. E., & Sharples, J. J. (2021). Intensifying Australian Heatwave Trends and Their Sensitivity to Observational Data. *Earth's Future, 9*, e2020EF001924. https://doi.org/10.1029/2020EF001924

Su, C.-H., Rennie, S., Torrance, J., Howard, E., Stassen, C., Lipson, M., Warren, R., Pepler, A., Dharssi, I., & Franklin, C. (2024). *BARRA-C2: Development of the kilometre-scale downscaled atmospheric reanalysis over Australia*. Bureau Research Report 097. Australian Bureau of Meteorology.

Su, C.-H., Torrance, J., Rennie, S., Howard, E., Stassen, C., Warren, R., et al. (2025). The Australian regional atmospheric reanalysis system, version 2 – BARRA2. *Journal of Southern Hemisphere Earth Systems Science, 75*, ES25032. https://doi.org/10.1071/ES25032

Weeding, B., Love, P., Beyer, K., Lucieer, A., & Remenyi, T. (2024). High-resolution projections of outdoor thermal stress in the twenty-first century: a Tasmanian case study. *International Journal of Biometeorology, 68*, 777–793. https://doi.org/10.1007/s00484-024-02622-8

Wuersch, L., Neher, A., Marino, F. E., Bamberry, L., & Pope, R. (2023). Impacts of Climate Change on Work Health and Safety in Australia: A Scoping Literature Review. *International Journal of Environmental Research and Public Health, 20*, 7004. https://doi.org/10.3390/ijerph20217004

---

# 12. One-sentence study statement

> **HeatScale-AU will apply an identical physically based WBGT calculation to hourly ERA5, BARRA-R2, and BARRA-C2 meteorology to determine when, where, and why atmospheric dataset choice and spatial scale change estimates of extreme heat stress and occupationally relevant workability across Australia.**
