import axios from "axios";
import {NotificationManager} from "react-notifications";
import {showLoading} from "react-global-loading";

const axiosClient = axios.create({
    baseURL: process.env.REACT_APP_API_BASE_URL || "http://192.168.1.104:8080", //"http://127.0.0.1:1880",
    timeout: 60000
});

function buildUrl(url, parameters){
    let qs = '';
    for(const key in parameters) {
        const value = parameters[key];
        qs += `${encodeURIComponent(key) }=${ encodeURIComponent(value) }&`;
    }
    if (qs.length > 0){
        qs = qs.substring(0, qs.length-1);
        url = `${url }?${ qs}`;
    }
    url = `.${url }`;
    return url;
}

export const apiRequest = (method, url, params, body, notificationText) => {
    showLoading(true);
    return axiosClient(
        {
            url: buildUrl(url, params),
            method: method,
            data: body
        })
        .then((response) => {
            console.log(response);
            if(notificationText !== undefined){
                NotificationManager.success(notificationText);
            }
            showLoading(false);
            return {status: response?.status, data: response?.data, error: null};
        })
        .catch((error) => {
            console.log(error);
            if (error.response) {
                // The request was made and the server responded with a status code
                // that falls out of the range of 2xx
                console.log(error.response.data);
                console.log(error.response.status);
            } else if (error.request) {
                // The request was made but no response was received
                // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                // http.ClientRequest in node.js
                console.log(error);
                console.log(error.request);
            }
            let message = error.request?.responseURL + " " + error.message ;
            let title = "Something went wrong!";
            if(error.response !== undefined) {
                title = error.response?.status + " " +error.response?.statusText;
            }
            showLoading(false);
            NotificationManager.error( message, title );
            return {
                status: error?.response?.status,
                data: null,
                error: error?.response?.data,
                statusText: error?.response?.statusText
            };
        })
}

export default apiRequest;
