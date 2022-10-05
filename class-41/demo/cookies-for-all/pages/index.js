import Head from 'next/head'
import { useAuth } from '../contexts/auth'
import useResource from '../hooks/useResource'

export default function Home() {

  const { user, login, logout } = useAuth();
  const { resources: stands } = useResource()

  return (
    <div>

      {user ? <>
        <p>User: {user && user.username}</p>
        <button onClick={logout}>Log Out</button>
        {stands && <StandTable stands={stands} />}
      </> : <button onClick={() => login("admin", "admin")} >Log In</button>}

    </div>
  )
}

function StandTable({ stands }) {
  return <p>{JSON.stringify(stands)}</p>
}
