import logo from './logo.svg';
import './App.css';
import Signup from './pages/user/signup';
import {BrowserRouter as Router ,Routes,Route} from 'react-router-dom'
import Home from './pages/home/Home';
import Login from './pages/user/login';
function App() {
  return (
    <Router>
      <Routes>
       <Route path='/sign-up' element={<Signup/>}></Route>
       <Route path='/login' element={<Login/>}></Route>
       <Route path='/main' element={<Home/>}></Route>
      </Routes>
    
    </Router>
    
  );
}

export default App;
