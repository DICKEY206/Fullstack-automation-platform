import { useState } from "react";
import API from "../utils/api";

export default function useAuth() {
  const [token, setToken] = useState(null);

  const login = async (email, password) => {
    const res = await API.post("/auth/login", { email, password });
    setToken(res.data.access_token);
    localStorage.setItem("token", res.data.access_token);
  };

  return { token, login };
}
