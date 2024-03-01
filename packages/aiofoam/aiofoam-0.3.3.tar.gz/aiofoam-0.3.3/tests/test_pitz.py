import pytest
import pytest_asyncio

import os
from pathlib import Path
from typing import Optional, Union

from aiofoam import Case

PITZ = Case(
    Path(os.environ["FOAM_TUTORIALS"]) / "incompressible" / "simpleFoam" / "pitzDaily"
)


@pytest_asyncio.fixture
async def pitz(tmp_path: Path) -> Case:
    return await PITZ.clone(tmp_path / PITZ.name)


@pytest.mark.asyncio
@pytest.mark.parametrize("script", [None, False])
@pytest.mark.parametrize("shell", [None, False, True, Path("/bin/sh")])
async def test_run(
    pitz: Case, script: Optional[bool], shell: Union[None, bool, Path]
) -> None:
    await pitz.run(script=script, shell=shell)
    await pitz.clean(script=script, shell=shell if shell is not None else False)
    await pitz.run(script=script, shell=shell)


@pytest.mark.asyncio
async def test_double_clean(pitz: Case) -> None:
    await pitz.clean()
    await pitz.clean(check=True)
    await pitz.run()


@pytest.mark.asyncio
async def test_run_script(pitz: Case) -> None:
    with pytest.raises(RuntimeError):
        await pitz.run(script=True)


@pytest.mark.asyncio
@pytest.mark.parametrize("script", [None, False])
async def test_run_parallel(pitz: Case, script: Optional[bool]) -> None:
    with pytest.raises(RuntimeError):
        await pitz.run(script=script, parallel=True)


@pytest.mark.asyncio
async def test_pyfoam(pitz: Case) -> None:
    pytest.importorskip("PyFoam")

    assert pitz.to_pyfoam().times == ["0"]
