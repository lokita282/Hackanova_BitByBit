import React from 'react'
import Sidebar from '../Components/Sidebar'
import Toolbar from '../Components/Toolbar'
import SpecialityGrid from '../Components/SpecialityGrid'
import Alan from '../Components/Alan'

const BookAppointments = () => {
  return (
    <>
      <Alan style={{ position: 'fixed' }} />
      <Toolbar />
      <Sidebar>
        book appointments
        {/* <SpecialityGrid /> */}
      </Sidebar>
    </>
  )
}

export default BookAppointments
