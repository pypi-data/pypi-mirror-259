import axios from "axios";
import { Url } from "./ApiComment";


export function ApiPost(path, body) {
    const x_user_email = localStorage.getItem('komodo')
    return new Promise((resolve, reject) => {
        let headers = {
            "Content-Type": "application/json",
            "X-User-Email": x_user_email,
        };
        axios
            .post(`/api/v1/${path}`, body, {
                headers: headers,
            })
            .then((response) => {
                resolve(response);
            })
            .catch((err) => {
                reject(err.response);
            });
    });
}

export function ApiGet(path, user) {
    return new Promise((resolve, reject) => {
        let headers = {
            "Content-Type": "application/json",
            "X-User-Email": user,
        };
        axios
            .get(`${Url}${path}`, {
                headers: headers,
            })
            .then((response) => {
                resolve(response);
            })
            .catch((err) => {
                reject(err.response);
            });
    });
}

export function ApiDelete(path, body) {
    const x_user_email = localStorage.getItem('komodo')
    return new Promise((resolve, reject) => {
        let headers = {
            "Content-Type": "application/json",
            "X-User-Email": x_user_email,
        };
        axios
            .delete(`/api/v1/${path}`, {
                headers: headers,
                data: body,
            })
            .then((response) => {
                resolve(response);
            })
            .catch((err) => {
                reject(err.response);
            });
    });
}

export function ApiPatch(path, body) {
    const x_user_email = localStorage.getItem('komodo')
    return new Promise((resolve, reject) => {
        let headers = {
            "Content-Type": "application/json",
            "X-User-Email": x_user_email,
        };
        axios
            .patch(`/api/v1/${path}`, body, {
                headers: headers,
            })
            .then((response) => {
                resolve(response);
            })
            .catch((err) => {
                reject(err.response);
            });
    });
}
export function ApiPut(path, body) {
    const x_user_email = localStorage.getItem('komodo')
    return new Promise((resolve, reject) => {
        let headers = {
            "Content-Type": "application/json",
            "X-User-Email": x_user_email,
        };
        axios
            .put(`/api/v1/${path}`, body, {
                headers: headers,
            })
            .then((response) => {
                resolve(response);
            })
            .catch((err) => {
                reject(err.response);
            });
    });
}