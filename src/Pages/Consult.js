import React from 'react'
import Grid from '@mui/material/Grid'
import Paper from '@mui/material/Paper'
import Sidebar from "../Components/Sidebar";
import Toolbar from "../Components/Toolbar";
import Deposits from "../Components/Deposits";

const Consult = () => {
  return (
    <>
      <Toolbar />
      <Sidebar >
        {/* Recent Deposits */}
        {/* <Grid item xs={12} md={4} lg={3}>
          <Paper
            sx={{
              p: 2,
              display: 'flex',
              flexDirection: 'column',
              height: 240,
            }}
          >
            <Deposits />
          </Paper>
        </Grid> */}
        consult
        {/* </Toolbar> */}
      </Sidebar>
    </>
  )
}

export default Consult