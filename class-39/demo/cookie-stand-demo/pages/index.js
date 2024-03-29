import Head from 'next/head';
import { useState } from 'react';
import { useAuth } from '../contexts/auth';
import useResource from '../hooks/useResource';

export default function Home() {

    const { user, login, logout } = useAuth();

    function loginHandler(newUser) {
        login(newUser.username, newUser.password);
    }


    return (
        <>
            <Head>
                <title>Cookie Stand Demo</title>
            </Head>
            <div>
                {
                    user ? <CookieStandAdmin user={user} logout={logout} /> : <LoginForm onLogin={loginHandler} />
                }

            </div>
        </>
    )
}

function CookieStandAdmin({ user, logout }) {

    const { resources, deleteResource } = useResource();

    return (
        <div>
            <p>Welcome {user.username}</p>

            <button onClick={logout}>Log Out</button>
            <CookieStandForm />
            <CookieStandTable stands={resources} deleteStand={deleteResource} />
        </div>
    );
}

function CookieStandForm() {

    const { user } = useAuth();
    const { createResource } = useResource();

    function handleSubmit(event) {
        event.preventDefault();
        const info = {
            location: event.target.location.value,
            minimum_customers_per_hour: parseInt(event.target.minimum.value),
            maximum_customers_per_hour: parseInt(event.target.maximum.value),
            average_cookies_per_sale: parseFloat(event.target.average.value),
            owner: user.id,
        };
        createResource(info);

    }

    return (
        <form onSubmit={handleSubmit}>
            <fieldset>
                <legend>Create Cookie Stand</legend>
                <input placeholder='location' name='location' />
                <input placeholder='minimum' name='minimum' />
                <input placeholder='maximum' name='maximum' />
                <input placeholder='average' name='average' />
                <button>create</button>
            </fieldset>
        </form>
    );
}


function CookieStandTable({ stands, deleteStand }) {
    return (
        <table className="my-8">
            <thead>
                <tr>
                    <th>Location</th>
                    <th>6 am</th>
                    <th>7 am</th>
                    <th>8 am</th>
                    <th>9 am</th>
                    <th>10 am</th>
                    <th>11 am</th>
                    <th>12 pm</th>
                    <th>1 pm</th>
                    <th>2 pm</th>
                    <th>3 pm</th>
                    <th>4 pm</th>
                    <th>5 pm</th>
                    <th>6 pm</th>
                    <th>7 pm</th>
                    <th>totals</th>
                </tr>
            </thead>
            <tbody>
                {stands.map(stand => (

                    <CookieStandRow key={stand.id} info={stand} deleteStand={deleteStand} />
                ))}
            </tbody>
        </table>
    );
}

function CookieStandRow({ info, deleteStand }) {

    function clickHandler() {
        deleteStand(info.id);
    }

    if (info.hourly_sales.length == 0) {
        // bunk data
        info.hourly_sales = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    }

    return (
        <tr>
            <td>{info.location} <button onClick={clickHandler}>[x]</button></td>
            {info.hourly_sales.map((slot, index) => <td key={index}>{slot}</td>)}
            <td>{info.hourly_sales.reduce((num, sum) => num + sum, 0)}</td>
        </tr>
    );
}


function LoginForm({ onLogin }) {

    function submitHandler(event) {
        event.preventDefault();
        const newUser = {
            username: event.target.username.value,
            password: event.target.password.value,
        };

        onLogin(newUser);
    }

    return (
        <form onSubmit={submitHandler}>
            <input placeholder="username" name="username" />
            <input type="password" name="password" placeholder="password" />
            <button>Log In</button>
        </form>
    );
}
