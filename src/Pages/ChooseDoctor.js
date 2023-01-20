import React from 'react'
import Sidebar from '../Components/Sidebar'
import Toolbar from '../Components/Toolbar'
import DoctorGrid from '../Components/DoctorGrid'

const ChooseDoctor = () => {
  return (
    <>
      <Toolbar />
      <Sidebar>
        <DoctorGrid />
      </Sidebar>
    </>
  )
}

export default ChooseDoctor
