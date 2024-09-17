import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import PageNotFound from "./pages/PageNotFound";
import HomePage from "./pages/HomePage";
import HandlePage from "./pages/HandlePage";

const App = () => (
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<HomePage />}></Route>
            <Route path="/handles/:username" element={<HandlePage />}></Route>
            <Route path="*" element={<PageNotFound />}></Route>
        </Routes>
    </BrowserRouter>
);

export default App;