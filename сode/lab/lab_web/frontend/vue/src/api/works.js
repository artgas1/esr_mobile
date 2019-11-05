import callAPI from "./api";

const Works = {
    get: data => callAPI('/api/works/', 'GET', data),
    create: data => callAPI("/api/works/", 'POST', data),
    Prices: {
        create: data => callAPI('/api/works_prices/', 'POST', data)
    }
}

export default Works;