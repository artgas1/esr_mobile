import callAPI from "./api";

const Operations = {
    get: data => callAPI('/api/operations/', 'GET', data),
    create: data => callAPI("/api/operations/", 'POST', data),
    Prices: {
        create: data => callAPI('/api/operations_prices/', 'POST', data)
    }
}

export default Operations;