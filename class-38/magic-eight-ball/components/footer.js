import Link from 'next/link';

export default function Footer() {
    return(
        <footer className="p-4 mt-8 bg-gray-500 test-gray-50">
            <Link href="/careers">
                <p className="text-2xl text-gray-50">Careers</p>
            </Link>
        </footer>
    );
}
