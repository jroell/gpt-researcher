import Image from "next/image";

const Header = () => {
  return (
    <div className="container h-[60px] px-4 pt-10 lg:h-[80px] lg:px-0">
      <div className="grid h-full grid-cols-12">
        <div className="col-span-5"></div>
        <div className="col-span-2 flex items-center justify-center">
          <a href="/">
            <Image
              src="/img/vurvey.png"
              alt="logo"
              width={440}
              height={20}
              className="lg:h-20 lg:w-20"
            />
          </a>
        </div>
      </div>
    </div>
  );
};

export default Header;
