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

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route exact path="/" element={<Toolbar />} />
          <Route path="/community" element={<Community />} />
          <Route path="/consult" element={<Consult />} />
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
