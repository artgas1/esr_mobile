import callAPI from './api'

const Auth = {
  tokenAuth: data => callAPI("/api/token_auth/", "POST", data),
};

export default Auth;
