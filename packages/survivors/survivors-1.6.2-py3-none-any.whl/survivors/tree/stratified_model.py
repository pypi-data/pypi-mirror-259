# import numpy as np
# from .. import constants as cnt
#
# from ..external import KaplanMeier, KaplanMeierZeroAfter
# from ..external import NelsonAalen
#
#
# class LeafModel(object):
#     survival_class = None
#     hazard_class = None
#
#     def __init__(self, weights_name=None):
#         if (self.survival_class is None) and (self.hazard_class is None):
#             raise Exception("There is no survival or hazard base class!")
#         self.shape = None
#         self.survival = None
#         self.hazard = None
#         self.features_predict = dict()
#         self.lists = dict()
#         self.default_bins = np.array([1, 10, 100, 1000])
#         self.weights_name = weights_name
#
#     def fit(self, X_node, need_features=[cnt.TIME_NAME, cnt.CENS_NAME], *args, **kwargs):
#         X_sub = X_node[need_features]
#         self.shape = X_sub.shape
#         self.features_predict = X_sub.mean(axis=0).to_dict()
#         self.lists = X_sub.to_dict(orient="list")
#         if self.weights_name is None:
#             self.weights = None
#         else:
#             if self.weights_name in X_node.columns:
#                 self.weights = X_node[self.weights_name].to_numpy()
#             else:
#                 self.weights = np.ones(self.shape[0])
#
#     def get_shape(self):
#         return self.shape
#
#     def predict_list_feature(self, feature_name):
#         if feature_name in self.lists.keys():
#             return np.array(self.lists[feature_name])
#         return None
#
#     def predict_feature(self, X=None, feature_name=None):
#         value = self.features_predict.get(feature_name)
#         if X is None:
#             return value
#         return np.repeat(value, X.shape[0], axis=0)
#
#     def predict_survival_at_times(self, X=None, bins=None):
#         if self.survival_class is None:
#             hf = self.predict_hazard_at_times(X=X, bins=bins)
#             sf = np.exp(-1 * hf)
#             return sf
#
#         if self.survival is None:
#             self.survival = self.survival_class()
#             self.survival.fit(self.lists[cnt.TIME_NAME],
#                               self.lists[cnt.CENS_NAME],
#                               self.weights)
#         if bins is None:
#             bins = self.survival.timeline
#         sf = self.survival.survival_function_at_times(bins)
#         if X is None:
#             return sf
#         return np.repeat(sf[np.newaxis, :], X.shape[0], axis=0)
#
#     def predict_hazard_at_times(self, X=None, bins=None):
#         if self.hazard_class is None:
#             sf = self.predict_survival_at_times(X=X, bins=bins)
#             hf = -1 * np.log(sf + 1e-100)
#             return hf
#
#         if self.hazard is None:
#             self.hazard = self.hazard_class()
#             self.hazard.fit(self.lists[cnt.TIME_NAME],
#                             self.lists[cnt.CENS_NAME],
#                             self.weights)
#         if bins is None:
#             bins = self.hazard.timeline
#         hf = self.hazard.cumulative_hazard_at_times(bins)
#         if X is None:
#             return hf
#         return np.repeat(hf[np.newaxis, :], X.shape[0], axis=0)
#
#
# class NormalizedLeafModel(LeafModel):
#     def fit(self, *args, **kwargs):
#         super().fit(*args, **kwargs)
#
#         durs = np.random.normal(np.mean(self.lists[cnt.TIME_NAME]),
#                                 np.std(self.lists[cnt.TIME_NAME]) / np.sqrt(2), 1000)
#         events = np.random.choice(self.lists[cnt.CENS_NAME], size=1000, replace=True)
#         self.lists[cnt.CENS_NAME] = events[durs > 0]
#         self.lists[cnt.TIME_NAME] = durs[durs > 0]
#         self.weights = np.ones_like(self.lists[cnt.TIME_NAME])
#
#
# class MeaningLeafModel(LeafModel):
#     def fit(self, *args, **kwargs):
#         super().fit(*args, **kwargs)
#         self.lists[cnt.TIME_NAME] = np.random.choice(self.lists[cnt.TIME_NAME], size=(2, 1000), replace=True).mean(axis=0)
#         self.lists[cnt.CENS_NAME] = np.random.choice(self.lists[cnt.CENS_NAME], size=1000, replace=True)
#         self.weights = np.ones_like(self.lists[cnt.TIME_NAME])
#
#
# class MixLeafModel(NormalizedLeafModel):
#     def fit(self, *args, **kwargs):
#         super().fit(*args, **kwargs)
#         self.lists[cnt.TIME_NAME] = np.random.choice(self.lists[cnt.TIME_NAME], size=(2, 1000), replace=True).mean(axis=0)
#         self.lists[cnt.CENS_NAME] = np.random.choice(self.lists[cnt.CENS_NAME], size=1000, replace=True)
#         self.weights = np.ones_like(self.lists[cnt.TIME_NAME])
#
#
# class BaseLeafModel(LeafModel):
#     survival_class = KaplanMeier
#     hazard_class = NelsonAalen
#
# class BaseLeafModelOnlySurv(LeafModel):
#     survival_class = KaplanMeier
#
# class BaseLeafModelOnlyHazard(LeafModel):
#     hazard_class = NelsonAalen
#
#
# class BaseNormalizedLeafModel(NormalizedLeafModel):
#     survival_class = KaplanMeierZeroAfter
#     hazard_class = NelsonAalen
#
#
# class BaseMeaningLeafModel(MeaningLeafModel):
#     survival_class = KaplanMeierZeroAfter
#     hazard_class = NelsonAalen
#
#
# class BaseMixLeafModel(MixLeafModel):
#     survival_class = KaplanMeierZeroAfter
#     hazard_class = NelsonAalen
#
#
# LEAF_MODEL_DICT = {
#     "base": BaseLeafModel,
#     "only_hazard": BaseLeafModelOnlyHazard,
#     "only_survive": BaseLeafModelOnlySurv,
#     "base_zero_after": BaseNormalizedLeafModel,
#     "base_normal": BaseNormalizedLeafModel,
#     "base_meaning": BaseMeaningLeafModel,
#     "base_mix": BaseMixLeafModel
# }
#
# #
# #
# # def epanechnikov_kernel(t, T, bandwidth=1.0):
# #     M = 0.75 * (1 - ((t - T) / bandwidth) ** 2)
# #     M[abs((t - T)) >= bandwidth] = 0
# #     return M
# #
# #
# # class LeafModel(object):
# #     def __init__(self):
# #         self.shape = None
# #         self.survival = None
# #         self.hazard = None
# #         self.features_predict = dict()
# #         self.lists = dict()
# #         self.default_bins = np.array([1, 10, 100, 1000])
# #
# #     def fit(self, X_node, need_features=[cnt.TIME_NAME, cnt.CENS_NAME], normalize=True):
# #         X_sub = X_node[need_features]
# #         self.shape = X_sub.shape
# #         self.features_predict = X_sub.mean(axis=0).to_dict()
# #         self.lists = X_sub.to_dict(orient="list")
# #
# #     def get_shape(self):
# #         return self.shape
# #
# #     def predict_list_feature(self, feature_name):
# #         if feature_name in self.lists.keys():
# #             return np.array(self.lists[feature_name])
# #         return None
# #
# #     def predict_feature(self, X=None, feature_name=None):
# #         value = self.features_predict.get(feature_name)
# #         if X is None:
# #             return value
# #         return np.repeat(value, X.shape[0], axis=0)
# #
# #     def predict_survival_at_times(self, X=None, bins=None):
# #         pass
# #
# #     def predict_hazard_at_times(self, X=None, bins=None):
# #         pass
# #
# #
# # class LeafSurviveAndHazard(LeafModel):
# #     def __init__(self):
# #         super().__init__()
# #
# #     def predict_survival_at_times(self, X=None, bins=None):
# #         if self.survival is None:
# #             self.survival = metr.get_survival_func(self.lists[cnt.TIME_NAME], self.lists[cnt.CENS_NAME])
# #         if bins is None:
# #             bins = self.default_bins
# #         sf = self.survival.survival_function_at_times(bins).to_numpy()
# #         if X is None:
# #             return sf
# #         return np.repeat(sf[np.newaxis, :], X.shape[0], axis=0)
# #
# #     def predict_hazard_at_times(self, X=None, bins=None):
# #         if self.hazard is None:
# #             self.hazard = metr.get_hazard_func(self.lists[cnt.TIME_NAME], self.lists[cnt.CENS_NAME])
# #         if bins is None:
# #             bins = self.default_bins
# #         hf = self.hazard.cumulative_hazard_at_times(bins).to_numpy()
# #         if X is None:
# #             return hf
# #         return np.repeat(hf[np.newaxis, :], X.shape[0], axis=0)
# #
# #
# # class LeafOnlyHazardModel(LeafSurviveAndHazard):
# #     def predict_survival_at_times(self, X=None, bins=None):
# #         hf = self.predict_hazard_at_times(X=X, bins=bins)
# #         sf = np.exp(-1*hf)
# #         if X is None:
# #             return sf
# #         return sf
# #
# #
# # class LeafOnlySurviveModel(LeafSurviveAndHazard):
# #     def predict_hazard_at_times(self, X=None, bins=None):
# #         sf = self.predict_survival_at_times(X=X, bins=bins)
# #         hf = -1*np.log(sf)
# #         if X is None:
# #             return hf
# #         return hf
# #
# #
# # class KaplanMeier:
# #     def __init__(self):
# #         self.timeline = None
# #         self.survival_function = None
# #         self.confidence_interval_ = None
# #         self.alpha = 0.05
# #
# #     def fit(self, durations, right_censor, weights=None):
# #         if weights is None:
# #             weights = np.ones(right_censor.shape)
# #         self.timeline = np.unique(durations)
# #
# #         dur_ = np.searchsorted(self.timeline, durations)
# #         hist_dur = np.bincount(dur_, weights=weights)
# #         self.hist_cens = np.bincount(dur_, weights=right_censor*weights)
# #         self.cumul_hist_dur = np.cumsum(hist_dur[::-1])[::-1]
# #         self.survival_function = np.hstack([1.0, np.cumprod((1.0 - self.hist_cens / (self.cumul_hist_dur)))])
# #
# #     def count_confidence_interval(self):
# #         ''' exponential Greenwood: https://www.math.wustl.edu/~sawyer/handouts/greenwood.pdf '''
# #         z = ss.norm.ppf(1 - self.alpha / 2)
# #         cumulative_sq_ = np.sqrt(np.hstack([0.0, np.cumsum(self.hist_cens / (self.cumul_hist_dur * (self.cumul_hist_dur - self.hist_cens)))]))
# #         np.nan_to_num(cumulative_sq_, copy=False, nan=0)
# #         v = np.log(self.survival_function)
# #         np.nan_to_num(v, copy=False, nan=0)
# #         self.confidence_interval_ = np.vstack([np.exp(v * np.exp(- z * cumulative_sq_ / v)),
# #                                                np.exp(v * np.exp(+ z * cumulative_sq_ / v))]).T
# #         np.nan_to_num(self.confidence_interval_, copy=False, nan=1)
# #
# #     def get_confidence_interval_(self):
# #         if self.confidence_interval_ is None:
# #             self.count_confidence_interval()
# #         return self.confidence_interval_
# #
# #     def survival_function_at_times(self, times):
# #         place_bin = np.digitize(times, self.timeline)
# #         return self.survival_function[np.clip(place_bin, 0, None)]
# #
# #
# # class FullProbKM(KaplanMeier):
# #     def fit(self, durations, right_censor, weights=None):
# #         durations = np.array(durations)
# #         right_censor = np.array(right_censor)
# #         if weights is None:
# #             weights = np.ones(right_censor.shape)
# #
# #         self.timeline = np.unique(durations)
# #         right_censor = right_censor.astype("bool")
# #         dur_ = np.searchsorted(self.timeline, durations)
# #
# #         self.hist_cens = np.bincount(dur_, weights=right_censor * weights)
# #         self.cumul_hist_dur = np.cumsum(self.hist_cens[::-1])[::-1]
# #         self.cumul_hist_dur[self.cumul_hist_dur == 0] = 1e-3  # Any cnt (in sf it becomes zero)
# #
# #         self.survival_function = np.hstack([1.0, np.cumprod((1.0 - self.hist_cens / (self.cumul_hist_dur)))])
# #
# #         N = right_censor.shape[0]
# #         Ncens = right_censor[~right_censor].shape[0]
# #         self.survival_function = Ncens / N + (1 - Ncens / N) * self.survival_function
# #
# #
# # class NelsonAalen:
# #     def __init__(self, smoothing=True):
# #         self.timeline = None
# #         self.survival_function = None
# #         self.smoothing = smoothing
# #
# #     def fit(self, durations, right_censor, weights=None):
# #         if weights is None:
# #             weights = np.ones(right_censor.shape)
# #         # The formula Stata: https://stats.stackexchange.com/questions/6670/
# #         self.bandwidth = np.std(durations)/(len(durations)**(1/5))
# #         self.timeline = np.unique(durations)
# #
# #         dur_ = np.searchsorted(self.timeline, durations)
# #         hist_dur = np.bincount(dur_, weights=weights)
# #         hist_cens = np.bincount(dur_, weights=right_censor*weights)
# #         cumul_hist_dur = np.cumsum(hist_dur[::-1])[::-1]
# #         if self.smoothing and all(weights == 1):
# #             cumul_hist_dur = cumul_hist_dur.astype("int")
# #             hist_cens = hist_cens.astype("int")
# #             cum_ = np.cumsum(1.0 / np.arange(1, np.max(cumul_hist_dur) + 1))
# #             hf = cum_[cumul_hist_dur - 1] - np.where(cumul_hist_dur - hist_cens - 1 >= 0,
# #                                                      cum_[cumul_hist_dur - hist_cens - 1], 0)
# #         else:
# #             hf = hist_cens / cumul_hist_dur
# #         self.hazard_function = np.hstack([0.0, np.cumsum(hf)])
# #
# #     def cumulative_hazard_at_times(self, times):
# #         place_bin = np.digitize(times, self.timeline)
# #         return self.hazard_function[np.clip(place_bin, 0, None)]
# #
# #     def smoothed_hazard_(self, bandwidth):
# #         timeline = self.timeline
# #         hazard_ = np.diff(self.hazard_function)
# #         sh = 1.0 / bandwidth * np.dot(epanechnikov_kernel(timeline[:, None],
# #                                                           timeline[None, :],
# #                                                           bandwidth), hazard_)
# #         return sh + np.max(sh) / self.timeline.shape[0]
# #
# #     def get_smoothed_hazard_at_times(self, bins):
# #         hazard_ = np.hstack([0.0, np.diff(self.cumulative_hazard_at_times(bins))])
# #         sh = 1.0 / self.bandwidth * np.dot(epanechnikov_kernel(bins[:, None],
# #                                                                bins[None, :],
# #                                                                self.bandwidth), hazard_)
# #         return sh + np.max(sh) / bins.shape[0]
# #
# #
# # class WeightSurviveModel(LeafModel):
# #     def __init__(self, weights_name="weights_obs"):
# #         self.weights_name = weights_name
# #         super().__init__()
# #
# #     def fit(self, X_node, need_features=[cnt.TIME_NAME, cnt.CENS_NAME], normalize=True):
# #         super().fit(X_node, need_features)
# #         #
# #         # if self.weights_name is None:
# #         #     self.weights = np.ones_like(X_node[cnt.TIME_NAME])
# #         # else:
# #         #     self.weights = X_node[self.weights_name].to_numpy()
# #
# #         # if normalize:
# #         #     self.old_durs = X_node[cnt.TIME_NAME]
# #         #     self.old_events = X_node[cnt.CENS_NAME]
# #         if normalize:
# #             durs = np.random.normal(np.mean(self.lists[cnt.TIME_NAME]),
# #                                     np.std(self.lists[cnt.TIME_NAME]) / np.sqrt(2), 1000)
# #             events = np.random.choice(self.lists[cnt.CENS_NAME], size=1000, replace=True)
# #             self.lists[cnt.CENS_NAME] = events[durs > 0]
# #             self.lists[cnt.TIME_NAME] = durs[durs > 0]
# #
# #         # self.lists[cnt.TIME_NAME] = np.vstack([np.random.choice(self.lists[cnt.TIME_NAME], size=1000, replace=True),
# #         #                                        np.random.choice(self.lists[cnt.TIME_NAME], size=1000, replace=True)]).mean(axis=0)
# #         # self.lists[cnt.CENS_NAME] = np.random.choice(self.lists[cnt.CENS_NAME], size=1000, replace=True)
# #
# #         self.weights = np.ones_like(self.lists[cnt.TIME_NAME])
# #
# #     def predict_survival_at_times(self, X=None, bins=None):
# #         if self.survival is None:
# #             self.survival = KaplanMeier()
# #             # print("WEI[:5] :", self.weights[:5])
# #             self.survival.fit(self.lists[cnt.TIME_NAME],
# #                               self.lists[cnt.CENS_NAME],
# #                               self.weights)
# #         if bins is None:
# #             bins = self.survival.timeline
# #         sf = self.survival.survival_function_at_times(bins)
# #         if X is None:
# #             return sf
# #         return np.repeat(sf[np.newaxis, :], X.shape[0], axis=0)
# #
# #     def predict_hazard_at_times(self, X=None, bins=None):
# #         if self.hazard is None:
# #             self.hazard = NelsonAalen()
# #             self.hazard.fit(self.lists[cnt.TIME_NAME],
# #                             self.lists[cnt.CENS_NAME],
# #                             self.weights)
# #         if bins is None:
# #             bins = self.hazard.timeline
# #         hf = self.hazard.cumulative_hazard_at_times(bins)
# #         if X is None:
# #             return hf
# #         return np.repeat(hf[np.newaxis, :], X.shape[0], axis=0)
# #
# #
# # class KaplanMeierZeroAfter(KaplanMeier):
# #     def fit(self, durations, right_censor, weights=None):
# #         # durs = np.hstack([durations, np.random.normal(np.mean(durations), np.std(durations), 100)])
# #         # events = np.hstack([right_censor, np.random.choice(right_censor, size=100, replace=True)])
# #
# #         # self.durs = np.random.normal(np.mean(durations), np.std(durations), 1000)  # / np.sqrt(2)
# #         # self.events = np.random.choice(right_censor, size=1000, replace=True)
# #
# #         # qs = np.quantile(durations, np.linspace(0.025, 0.975, 100))
# #         # self.durs = np.random.choice(qs, size=1000, replace=True)
# #         # self.events = np.random.choice(right_censor, size=1000, replace=True)
# #
# #         self.durs = np.array(durations)
# #         self.events = np.array(right_censor)
# #
# #         super().fit(self.durs, self.events)
# #
# #     def survival_function_at_times(self, times):
# #         place_bin = np.searchsorted(self.timeline, times)
# #         # place_bin = np.digitize(times, self.timeline)  # -1
# #         sf = self.survival_function[np.clip(place_bin, 0, None)]
# #         sf[times > self.timeline[-1]] = 0
# #         sf[times < self.timeline[0]] = 1
# #         return sf
# #
# #
# # class NelsonAalenSample(NelsonAalen):
# #     def fit(self, durations, right_censor, weights=None):
# #         # self.durs = np.random.normal(np.mean(durations), np.std(durations), 1000)  # / np.sqrt(2)
# #         # self.events = np.random.choice(right_censor, size=1000, replace=True)
# #
# #         self.durs = np.array(durations)
# #         self.events = np.array(right_censor)
# #
# #         super().fit(self.durs, self.events)
# #
# # class WeightSurviveModelZeroAfter(WeightSurviveModel):
# #     def predict_survival_at_times(self, X=None, bins=None):
# #         if bins is None:
# #             bins = self.default_bins
# #         if self.survival is None:
# #             self.survival = KaplanMeierZeroAfter()
# #             self.survival.fit(self.lists[cnt.TIME_NAME],
# #                               self.lists[cnt.CENS_NAME],
# #                               self.weights)
# #         sf = self.survival.survival_function_at_times(bins)
# #         if X is None:
# #             return sf
# #         return np.repeat(sf[np.newaxis, :], X.shape[0], axis=0)
# #
# #     def predict_hazard_at_times(self, X=None, bins=None):
# #         if self.hazard is None:
# #             self.hazard = NelsonAalenSample()
# #             self.hazard.fit(self.lists[cnt.TIME_NAME],
# #                             self.lists[cnt.CENS_NAME],
# #                             self.weights)
# #         if bins is None:
# #             bins = self.hazard.timeline
# #         hf = self.hazard.cumulative_hazard_at_times(bins)
# #         if X is None:
# #             return hf
# #         return np.repeat(hf[np.newaxis, :], X.shape[0], axis=0)
# #
# #     def predict_feature(self, X=None, feature_name=None):
# #         self.predict_survival_at_times()
# #         if not(X is None) and feature_name == "time":
# #             return np.repeat(np.trapz(self.survival.survival_function, np.hstack([0, self.survival.timeline])), X.shape[0], axis=0)
# #         return super().predict_feature(X, feature_name)
# #
# #
# # class WeightOnlySurviveModelZeroAfter(WeightSurviveModelZeroAfter):
# #     def predict_hazard_at_times(self, X=None, bins=None):
# #         sf = self.predict_survival_at_times(X, bins)
# #         return -1*np.log(sf + 1e-100)
# #
# #
# # class BaseWeightMeaningSurviveModel(WeightSurviveModelZeroAfter):
# #     def __init__(self, weights_name=None):
# #         self.weights_name = weights_name
# #         super().__init__()
# #
# #     def fit(self, X_node, need_features=[cnt.TIME_NAME, cnt.CENS_NAME], normalize=True):
# #         super().fit(X_node, need_features)
# #         self.lists[cnt.TIME_NAME] = np.vstack([np.random.choice(self.lists[cnt.TIME_NAME], size=1000, replace=True),
# #                                                np.random.choice(self.lists[cnt.TIME_NAME], size=1000, replace=True)]).mean(axis=0)
# #         self.lists[cnt.CENS_NAME] = np.random.choice(self.lists[cnt.CENS_NAME], size=1000, replace=True)
# #
# #         self.weights = np.ones_like(self.lists[cnt.TIME_NAME])
# #
# # class BaseWeightNormSurviveModel(WeightSurviveModelZeroAfter):
# #     def __init__(self, weights_name=None):
# #         self.weights_name = weights_name
# #         super().__init__()
# #
# #     def fit(self, X_node, need_features=[cnt.TIME_NAME, cnt.CENS_NAME], normalize=True):
# #         super().fit(X_node, need_features)
# #         durs = np.random.normal(np.mean(self.lists[cnt.TIME_NAME]),
# #                                 np.std(self.lists[cnt.TIME_NAME]), 1000)
# #         events = np.random.choice(self.lists[cnt.CENS_NAME], size=1000, replace=True)
# #         self.lists[cnt.CENS_NAME] = events[durs > 0]
# #         self.lists[cnt.TIME_NAME] = durs[durs > 0]
# #
# #         self.weights = np.ones_like(self.lists[cnt.TIME_NAME])
# #
# # class BaseFastOnlySurviveModelZeroAfter(WeightOnlySurviveModelZeroAfter):
# #     def __init__(self):
# #         super().__init__(weights_name=None)
# #
# # class BaseFastSurviveModelZeroAfter(WeightSurviveModelZeroAfter):
# #     def __init__(self):
# #         super().__init__(weights_name=None)
# #
# #
# # class BaseFastSurviveModel(WeightSurviveModel):
# #     def __init__(self):
# #         super().__init__(weights_name=None)
# #
# #
# # class FullProbSurviveModel(BaseFastSurviveModel):
# #     def predict_survival_at_times(self, X=None, bins=None):
# #         if bins is None:
# #             bins = self.default_bins
# #         if self.survival is None:
# #             self.survival = FullProbKM()
# #             self.survival.fit(self.lists[cnt.TIME_NAME],
# #                               self.lists[cnt.CENS_NAME],
# #                               self.weights)
# #         sf = self.survival.survival_function_at_times(bins)
# #         if X is None:
# #             return sf
# #         return np.repeat(sf[np.newaxis, :], X.shape[0], axis=0)
# #
# #
# # LEAF_MODEL_DICT = {
# #     "base": LeafSurviveAndHazard,
# #     "only_hazard": LeafOnlyHazardModel,
# #     "only_survive": LeafOnlySurviveModel,
# #     "wei_survive": WeightSurviveModel,
# #     "base_fast": BaseFastSurviveModel,
# #     "base_zero_after": BaseFastSurviveModelZeroAfter,
# #     "base_only_zero_after": BaseFastOnlySurviveModelZeroAfter,
# #     "wei_zero_after": WeightSurviveModelZeroAfter,
# #     "fullprob_fast": FullProbSurviveModel,
# #     "base_meaning": BaseWeightMeaningSurviveModel,
# #     "base_normal": BaseWeightNormSurviveModel
# # }
