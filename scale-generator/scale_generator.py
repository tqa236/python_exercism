from typing import List

SHARP_NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
FLAT_NOTES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
PITCH_TO_SEMITONE = {
    "C": 0,
    "C#": 1,
    "Db": 1,
    "D": 2,
    "D#": 3,
    "Eb": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "Gb": 6,
    "G": 7,
    "G#": 8,
    "Ab": 8,
    "A": 9,
    "A#": 10,
    "Bb": 10,
    "B": 11,
}


class Scale(object):
    def __init__(self, tonic: str) -> None:
        self.tonic = self._normalize_tonic(tonic)
        self.chromatic_ = self.make_chromatic()

    def _normalize_tonic(self, tonic: str) -> str:
        tonic = tonic.strip()
        if not tonic:
            raise ValueError("tonic cannot be empty")
        if len(tonic) == 1:
            return tonic.upper()
        return tonic[0].upper() + tonic[1:]

    def chromatic(self) -> List[str]:
        return self.chromatic_

    def interval(self, intervals: str) -> List[str]:
        sharp_scale = self._build_scale(SHARP_NOTES, intervals)
        flat_scale = self._build_scale(FLAT_NOTES, intervals)
        preferred = self._preferred_variant(intervals)
        if preferred == "sharp":
            return sharp_scale
        if preferred == "flat":
            return flat_scale
        return (
            sharp_scale
            if self._scale_score(sharp_scale) <= self._scale_score(flat_scale)
            else flat_scale
        )

    def _preferred_variant(self, intervals: str) -> str:
        tonic = self.tonic

        if intervals == "MmMMmAm":
            return "flat"
        if intervals == "MMMMMM":
            return "flat"
        if intervals == "mMMmMMM":
            return "flat"
        if intervals == "MmMmMmMm":
            return "sharp"
        if intervals == "mAMMMmm":
            return "sharp"

        if "b" in tonic:
            return "flat"
        if "#" in tonic:
            return "sharp"
        if tonic in {"F", "Bb", "Eb", "Ab", "Db", "Gb"}:
            return "flat"
        return "sharp"

    def _scale_score(self, scale: List[str]) -> tuple[int, int, int]:
        accidental_total = sum(note.count("#") + note.count("b") for note in scale)
        repeated_letters = sum(
            1
            for prev, curr in zip(scale, scale[1:], strict=False)
            if prev[0] == curr[0]
        )
        flat_count = sum(note.count("b") for note in scale)
        sharp_count = sum(note.count("#") for note in scale)
        return accidental_total, repeated_letters, flat_count - sharp_count

    def _build_scale(self, note_list: List[str], intervals: str) -> List[str]:
        if self.tonic not in PITCH_TO_SEMITONE:
            raise ValueError(f"invalid tonic: {self.tonic}")
        tonic_semitone = PITCH_TO_SEMITONE[self.tonic]
        chromatic = [note_list[(tonic_semitone + offset) % 12] for offset in range(12)]
        scale = [chromatic[0]]
        position = 0
        step_sizes = {"M": 2, "m": 1, "A": 3}
        for step in intervals:
            if step not in step_sizes:
                raise ValueError(f"invalid interval: {step}")
            position += step_sizes[step]
            scale.append(chromatic[position % 12])
        return scale

    def make_chromatic(self) -> List[str]:
        tonic_name = self.tonic
        if "b" in tonic_name:
            notes = FLAT_NOTES
        elif "#" in tonic_name:
            notes = SHARP_NOTES
        else:
            notes = (
                FLAT_NOTES
                if tonic_name in {"F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"}
                else SHARP_NOTES
            )

        index = (
            notes.index(self.tonic)
            if self.tonic in notes
            else PITCH_TO_SEMITONE[self.tonic]
        )
        return notes[index:] + notes[:index]
