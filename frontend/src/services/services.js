import apiRequest from "../utils/axios/request";

export const createCampaign = (body) => apiRequest("post", "/api/campaign",null, body
    , "Campaign created successfully!");
export const getCampaign = (campaignId) => apiRequest("get", "/api/campaign/"+ campaignId);
export const getCampaigns = () => apiRequest("get", "/api/campaign");


export const createAdset = (body) => apiRequest("post", "/api/adset",null, body
    , "Adset created successfully!");
export const getAdset = (adsetId) => apiRequest("get", "/api/adset/"+ adsetId);
export const getAdsets = () => apiRequest("get", "/api/adset");

export const getAdsetInsight = (adsetId) => apiRequest("get", "/api/insights/"+ adsetId);

export const createAd = (body) => apiRequest("post", "/api/ad",null, body
    , "Ad created successfully!");
export const getAd = (adId) => apiRequest("get", "/api/ad/"+ adId);
export const getAds = () => apiRequest("get", "/api/ad");

export const createAdCreative = (body) => apiRequest("post", "/api/adcreative",null, body
    , "AdCreative created successfully!");
export const getAdCreative = (adCreativeId) => apiRequest("get", "/api/adcreative/"+ adCreativeId);
export const getAdCreatives = () => apiRequest("get", "/api/adcreative");

export const getAdPreview = (adId) => apiRequest("get", "/api/preview/"+ adId);
