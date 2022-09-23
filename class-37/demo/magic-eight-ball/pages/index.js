import Head from 'next/head';
import { replies } from '../data';
import { useState } from 'react';

export default function Home() {
    const [reply, setReply] = useState('Ask me anything');

    function questionAskedHandler(event) {
        event.preventDefault();
        const randomReply = replies[Math.floor(Math.random() * replies.length)];
        setReply(randomReply);
    }

    return (
        <div>
            <Head>
                <title>Magic 8 Ball</title>
            </Head>
            <header className="flex items-center p-4 justify-between bg-gray-500 text-gray-50">
                <h1 className="text-4xl">Magic 8 Ball</h1>
                <p>0 questions answered</p>
            </header>
            <main>
                <form onSubmit={questionAskedHandler} className="flex w-1/2 p-2 mx-auto my-4 bg-gray-200">
                    <input name="question" className="flex-auto pl-1"/>
                    <button className="px-2 py-1 bg-gray-500 text-gray-50">Ask</button>
                </form>
                <div className="w-96 h-96 mx-auto my-4 bg-gray-900 rounded-full">
                    <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
                        <p className="text-xl text-center" >{ reply }</p>
                    </div>
                </div>
            </main>
            <footer className="p-4 mt-8 bg-gray-500 test-gray-50">
                <p className="text-2xl text-gray-50">Careers</p>
            </footer>
        </div>);

}
