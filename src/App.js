import './App.css';
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Outlet,
  Navigate,
} from 'react-router-dom'
import Sidebar from './Components/Sidebar'
import Toolbar from './Components/Toolbar'

import Dashboard from './Pages/Dashboard'
import Community from './Pages/Community'
import Consult from './Pages/Consult'
import Support from './Pages/Support'
import Exercise from './Pages/Exercise'
import ChooseSpeciality from './Pages/ChooseSpeciality'
import ChooseDoc from './Pages/ChooseDoctor'
import BookAppointments from './Pages/BookAppointments'
// import BookAppointments from './Pages/BookAppointments'
import MyAccount from './Pages/MyAccount'
import Alan from './Components/Alan'

function App() {
  return (
    <>
      
      <Router>
        <Routes>
          <Route path="/" element={<Consult />} />
          <Route path="/chooseSpeciality" element={<ChooseSpeciality />} />
          <Route path="/chooseDoc" element={<ChooseDoc />} />
          <Route path="/bookAppt" element={<BookAppointments />} />
          <Route path="/myAccount" element={<MyAccount />} />
          <Route path="/community" element={<Community />} />
          <Route path="/support" element={<Support />} />
          <Route path="/exercise" element={<Exercise />} />
          {/* <Route path="/appguide" element={<AppGuide />} />
          <Route path="/webinars" element={<Webinars />} />
          <Route path="/task" element={<PerformTask />} /> */}
        </Routes>
      </Router>
    </>
  )
}

export default App;
