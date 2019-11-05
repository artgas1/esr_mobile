import callAPI from "./api";
export default {
    Works: {
        get: () => callAPI('/api/works_price_lists/', 'GET'),
        create: data => callAPI('/api/works_price_lists/', 'POST', data)
    },
    Operations: {
        get: () => callAPI('/api/operations_price_lists/', 'GET'),
        create: data => callAPI('/api/operations_price_lists/', 'POST', data)
    }
}