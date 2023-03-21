import { Navigate, Route, Routes } from "react-router-dom";
import './App.scss';

import LoginPage from "./pages/login";
import NotFoundPage from "./pages/not-found";
import RegistroPage from "./pages/registro";


import './styles/home.scss';
import './styles/menu.scss';
import './styles/pace_loader.scss';
import './styles/style.scss';
import './styles/tarjeta.scss';

function App() {
	return (
		<>
			<Routes>
				<Route path="/login" element={<LoginPage />} />
				<Route path="/registro" element={<RegistroPage />} />
				<Route path="/" element={<Navigate to='/login' />} />
				<Route path="*" element={<NotFoundPage />} />
			</Routes>
		</>
	);
}

export default App;
