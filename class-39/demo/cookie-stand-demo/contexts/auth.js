
import { createContext, useContext, useState } from "react";
import axios from "axios";
import jwt from "jsonwebtoken";


const AuthContext = createContext();

export function useAuth() {

    const auth = useContext(AuthContext);
    if (!auth) {
        throw new Error("You forgot to set up AuthProvider!");
    }

    return auth;

}

export function AuthProvider(props) {

    const [state, setState] = useState({
        tokens: null,
        user: null,
        login,
        logout,
    });

    async function login(username, password) {

        const loginUrl = process.env.NEXT_PUBLIC_API_URL + "/api/token/";

        const response = await axios.post(loginUrl, { username, password });

        const decodedAccess = jwt.decode(response.data.access);

        const newState = {
            tokens: response.data,
            user: {
                username: decodedAccess.username,
                email: decodedAccess.email,
                id: decodedAccess.user_id,
            }
        }

        setState(prevState => ({ ...prevState, ...newState }));
    }

    function logout() {
        const newState = {
            tokens: null,
            user: null
        }

        setState(prevState => ({ ...prevState, ...newState }));
    }

    return (
        <AuthContext.Provider value={state}>
            {props.children}
        </AuthContext.Provider>
    );

}
